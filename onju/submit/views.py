from django.shortcuts import render
from submit.forms import CodeSubmissionForm
from django.conf import settings
import os
import uuid
import subprocess
from pathlib import Path

def code_view(request, user_id):
    form = CodeSubmissionForm()  # Create an instance of your form
    context = {'user_id': user_id, 'form': form}
    return render(request, 'mindex.html', context)

def submit(request, user_id):
    if request.method == "POST":
        form = CodeSubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.user_id = user_id
            output = run_code(
                submission.language, submission.code, submission.input_data
            )
            submission.output_data = output
            submission.save()

            # Compare output with desired output
            is_correct = submission.output_data.strip() == submission.desired_output.strip()

            context = {
                'user_id': user_id,
                "submission": submission,
                'is_correct': is_correct,
                'error_message': output if not is_correct else None  # Display error message if not correct
            }
            return render(request, "result.html", context)
    else:
        form = CodeSubmissionForm()
    context = {'user_id': user_id, 'form': form}
    return render(request, 'mindex.html', context)


def run_code(language, code, input_data):
    project_path = Path(settings.BASE_DIR)
    directories = ["codes", "inputs", "outputs"]

    for directory in directories:
        dir_path = project_path / directory
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)

    codes_dir = project_path / "codes"
    inputs_dir = project_path / "inputs"
    outputs_dir = project_path / "outputs"

    unique = str(uuid.uuid4())

    code_file_name = f"{unique}.{language}"
    input_file_name = f"{unique}.txt"
    output_file_name = f"{unique}.txt"

    code_file_path = codes_dir / code_file_name
    input_file_path = inputs_dir / input_file_name
    output_file_path = outputs_dir / output_file_name

    with open(code_file_path, "w") as code_file:
        code_file.write(code)

    with open(input_file_path, "w") as input_file:
        input_file.write(input_data)

    with open(output_file_path, "w") as output_file:
        pass  # This will create an empty output file

    compile_result = None
    execution_result = None

    if language == "cpp":
        executable_path = codes_dir / unique
        compile_result = subprocess.run(
            ["g++", str(code_file_path), "-o", str(executable_path)],
            capture_output=True,
            text=True,
        )
        if compile_result.returncode == 0:
            with open(input_file_path, "r") as input_file:
                with open(output_file_path, "w") as output_file:
                    execution_result = subprocess.run(
                        [str(executable_path)],
                        stdin=input_file,
                        stdout=output_file,
                        stderr=subprocess.PIPE,
                        text=True,
                    )
    elif language == "py":
        try:
            execution_result = subprocess.run(
                ["python", str(code_file_path)],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=10,  # Timeout after 10 seconds
            )
        except subprocess.TimeoutExpired:
            return "Execution Timeout: The program took too long to execute."
        except Exception as e:
            return f"Execution Error: {str(e)}"

    if compile_result and compile_result.returncode != 0:
        error_message = compile_result.stderr
        return f"Compilation Error:\n{error_message}"

    if execution_result:
        if execution_result.returncode != 0:
            error_message = execution_result.stderr
            return f"Runtime Error:\n{error_message}"

        with open(output_file_path, "r") as output_file:
            output_data = output_file.read()
            return output_data

    return "Unknown Error"