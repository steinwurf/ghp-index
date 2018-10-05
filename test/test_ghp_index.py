
def test_ghp_index(testdirectory):
    a_dir = testdirectory.mkdir('a')
    b_dir = testdirectory.mkdir('b')
    c_dir = testdirectory.mkdir('c')
    d_dir = testdirectory.mkdir('d')

    t100_dir = testdirectory.mkdir('1.0.0')
    t110_dir = testdirectory.mkdir('1.1.0')
    t200_dir = testdirectory.mkdir('2.0.0')

    testdirectory.run('ghp_index --docspath . --outpath .'
                      ' --project_name test --github_url="github.com"')

    assert testdirectory.contains_file('index.html')
