## Log processing coding exercise
### Name: Jonathan Hickman
### Date: 2021-10-10

Simple python application that takes a file path and parses it with a known comma delineated schema. 

Only requirement is a module called [attrs](https://www.attrs.org/en/stable/) which reduces boiler plate code without sacrificing performance.


<hr>

## Setup

Code is written to target `>3.8.9`

### Virtual Environment

```
python3 -m venv .venv
source ./.venv/bin/activate
```

### Install dependencies

```
pip install -r requirements.txt
```

<hr>

## Running project 
<br>

`python Main.py <file_path>`

e.g. `python Main.py ~/dev/jhickman-python-log-parsing/fake_msgs.log`

Code output should resemble the following:
```
n32: Average: 92.52 Max: 100.0 Min: 73.0
n29: Average: 87.23 Max: 100.0 Min: 46.0
n30: Average: 85.83 Max: 100.0 Min: 44.0
...
```

Execute tests: 

`python -m unittest MetricCollecting.tests.TestProcessor -v`


## Project Layout

`./app` - Contains core processing code

`./tests` - Contains unit tests 

Primary entrypoint is from the root folder in `Main.py` which takes a filepath argument and calls `process_log` with output formatting. 
