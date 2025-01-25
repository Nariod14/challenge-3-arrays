import pytest

import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/src')

from array_duplicator import findDuplicates, removeDuplicates, countOccurrences


def test_find_duplicates():
    assert findDuplicates([1, 2, 3, 3, 4, 4, 5]) == [3, 4]
    assert findDuplicates([1, 2, 3, 4, 5]) == []
    assert findDuplicates([1, 1, 1, 1, 1]) == [1]
    assert findDuplicates([]) == []
    assert findDuplicates([1]) == []
    
    assert findDuplicates(["a", "b", "c", "c", "d"]) == ["c"]
    assert findDuplicates(["a", "b", "c", "d"]) == []
    assert findDuplicates(["a", "a", "a", "a", "a"]) == ["a"]
    assert findDuplicates(["a"]) == []

    assert findDuplicates([1, 2, 3, 4, "a", "b", "c", "d"]) == []
    assert findDuplicates([1, 2, 3, 4, "a", "a", "a", "a", "a"]) == ["a"]
    assert findDuplicates([1, 2, 2, 4, "a"]) == [2]
    assert findDuplicates([1, 2, 3, 4, "a"]) == []
    
    with pytest.raises(TypeError):
        findDuplicates(None)
    
    with pytest.raises(TypeError):
        findDuplicates(1)
        
    with pytest.raises(TypeError):
        findDuplicates("a")
        
    with pytest.raises(ValueError):
        findDuplicates([1, 2, 3, None, 4, 5])

def test_remove_duplicates():
    assert removeDuplicates([1, 2, 3, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
    assert removeDuplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert removeDuplicates([1, 1, 1, 1, 1]) == [1]
    assert removeDuplicates([]) == []
    assert removeDuplicates([1]) == [1]
    
    assert removeDuplicates(["a", "b", "c", "c", "d"]) == ["a", "b", "c", "d"]
    assert removeDuplicates(["a", "b", "c", "d"]) == ["a", "b", "c", "d"]
    assert removeDuplicates(["a", "a", "a", "a", "a"]) == ["a"]
    assert removeDuplicates(["a"]) == ["a"]
    
    assert removeDuplicates([1, 2, 3, 4, "a", "b", "c", "d"]) == [1, 2, 3, 4, "a", "b", "c", "d"]
    assert removeDuplicates([1, 2, 3, 4, "a", "a", "a", "a", "a"]) == [1, 2, 3, 4, "a"]
    assert removeDuplicates([1, 2, 3, 4, "a"]) == [1, 2, 3, 4, "a"]
    
    
    with pytest.raises(TypeError):
        removeDuplicates(None)
    
    with pytest.raises(TypeError):
        removeDuplicates(1)
        
    with pytest.raises(TypeError):
        removeDuplicates("a")
    
    with pytest.raises(ValueError):
        findDuplicates([1, 2, 3, None, 4, 5])
        
def test_count_occurrences():
    assert countOccurrences([1, 2, 3, 3, 4, 4, 5]) == {1: 1, 2: 1, 3: 2, 4: 2, 5: 1}
    assert countOccurrences([1, 2, 3, 4, 5]) == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
    assert countOccurrences([1, 1, 1, 1, 1]) == {1: 5}
    assert countOccurrences([]) == {}
    assert countOccurrences([1]) == {1: 1}
    
    assert countOccurrences(["a", "b", "c", "c", "d"]) == {"a": 1, "b": 1, "c": 2, "d": 1}
    assert countOccurrences(["a", "b", "c", "d"]) == {"a": 1, "b": 1, "c": 1, "d": 1}
    assert countOccurrences(["a", "a", "a", "a", "a"]) == {"a": 5}
    assert countOccurrences(["a"]) == {"a": 1}
    
    assert countOccurrences([1, 2, 3, 4, "a", "b", "c", "d"]) == {1: 1, 2: 1, 3: 1, 4: 1, "a": 1, "b": 1, "c": 1, "d": 1}
    assert countOccurrences([1, 2, 3, 4, "a", "a", "a", "a", "a"]) == {1: 1, 2: 1, 3: 1, 4: 1, "a": 5}
    assert countOccurrences([1, 2, 3, 4, "a"]) == {1: 1, 2: 1, 3: 1, 4: 1, "a": 1}
    
    
    with pytest.raises(TypeError):
        countOccurrences(None)
    
    with pytest.raises(TypeError):
        countOccurrences(1)
        
    with pytest.raises(TypeError):
        countOccurrences("a")
        
    with pytest.raises(ValueError):
        findDuplicates([1, 2, 3, None, 4, 5])
        

if __name__ == "__main__":
    test_find_duplicates()
    test_remove_duplicates()
    test_count_occurrences()