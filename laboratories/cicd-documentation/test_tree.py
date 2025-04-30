# si scrieti cel putin 2 unit teste pentru functia _find (din tree.py)
import pytest

from tree import Tree

def test_find_existing_node():
    """Test finding an existing node in the tree."""
    tree = Tree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    
    found_node = tree.find(3)
    
    assert found_node is not None
    assert found_node.data == 3

def test_find_non_existing_node():
    """Test finding a non-existing node in the tree."""
    tree = Tree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    
    found_node = tree.find(10)
    
    assert found_node is None

def test_find_root_node():
    """Test finding the root node in the tree."""
    tree = Tree()
    
    # Add multiple nodes
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(1)

    # Find the root node (try class.getroot())
    root_node = tree.getRoot()
    assert root_node is not None
    assert root_node.data == 5

def test_find_left_child():
    """Test finding a left child node in the tree."""
    tree = Tree()
    
    # Add multiple nodes
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(1)

    # Find the left child node
    left_child_node = tree.find(3)
    assert left_child_node is not None
    assert left_child_node.data == 3

def test_find_right_child():
    """Test finding a right child node in the tree."""
    tree = Tree()
    
    # Add multiple nodes
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(9)

    # Find the right child node
    right_child_node = tree.find(7)
    assert right_child_node is not None
    assert right_child_node.data == 7


