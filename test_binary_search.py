from binary_search import binary_search

if __name__ == '__main__':
    assert binary_search([1], 1)
    assert binary_search([1,2,3], 2)
    assert binary_search([1,2,3,4], 4)
    assert not binary_search([], 1)
    assert not binary_search([2], 1)
    assert not binary_search([2, 3, 4], 1)
    assert not binary_search([2, 3, 4], 5)
    assert not binary_search([1, 3, 4, 5], 2)
