
def test_ghp_index(testdirectory):
    a_dir = testdirectory.mkdir('a')
    b_dir = testdirectory.mkdir('b')
    c_dir = testdirectory.mkdir('c')
    d_dir = testdirectory.mkdir('d')

    testdirectory.run('ghp_index --docspath . --outpath .')

    assert testdirectory.contains_file('index.html')
