import pytest
from deepClassifier.utils import read_yaml
from pathlib import Path
from box import ConfigBox
from ensure.main import EnsureError

yaml_file = [
    "tests/data/empty.yaml",
    "tests/data/demo.yaml"
]

def test_read_yaml_empty():
    with pytest.raises(ValueError):
        read_yaml(Path(yaml_file[0]))
        
def test_read_yaml_return_type():
    response = read_yaml(Path(yaml_file[-1]))   
    assert isinstance(response,ConfigBox)

@pytest.mark.parametrize("path_to_yaml",yaml_files)
def test_read_yaml_bad_type():
    with pytest.raises(EnsureError):
        read_yaml(Path(path_yaml_file))