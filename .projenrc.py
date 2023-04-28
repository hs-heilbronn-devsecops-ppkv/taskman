from projen.python import PythonProject

project = PythonProject(
    author_email="nico@nicolas-byl.io",
    author_name="Nicolas Byl",
    module_name="taskman",
    name="taskman",
    version="0.1.0",
    deps=[
        'fastapi',
        'uvicorn[standard]',
        'httpx'
    ],
    dev_deps=[
        'attrs',
        'pylint',
        'pytest',
        'pytest-cov',
    ],
    github=False,
)

project.add_git_ignore('.idea')

dev_task = project.add_task('dev')
dev_task.exec('uvicorn taskman.main:app --reload')


project.synth()