from quiz_struct import QuizQuestion

quiz_header = "PCAP Programming Essentials in Python Essentials 2 PE2 Module 1"
quiz_description = """
    PCAP Programming Essentials in Python Essentials 2 PE2 Module 1"""
quiz_information = """
    PCAP Programming Essentials in Python Essentials 2 PE2 Module 1  
    Test Quizzes Exam Answers"""
quiz_link = "[Click here to learn more >](https://pythoninstitute.org/pcap)"

# Define the questions, correct answers, and possible answers
quiz = {
    1: QuizQuestion(
        '''Knowing that a function named fun() resides in a module named mod , choose thecorrect way to import it:''',
        None,
        None,
        None,
        {'A': 'from mod import fun', 'B': 'import fun from mod', 'C': 'from fun import mod', 'D': 'import fun'},
        ['A'],
    ),
    2: QuizQuestion('''What is the expected output of the following code?''',
                    '''
                    from random import randint
                    for i in range(2):  
                        print (randint(1,2), end='')''',
                    None,
                    None,
                    {'A': '12, or 21',
                     'B': 'there are millions of possible combinations, and the exact output cannot be predicted',
                     'C': '12', 'D': '11, 12, 21, or 22'},
                    ['D'],
                    ),
    3: QuizQuestion(
        '''During the first import of a module, Python deploys the pyc files in the directory called:''',
        None,
        None,
        None,
        {'A': 'mymodules', 'B': '__init__', 'C': 'hashbang', 'D': '__pycache__'},
        ['D'],
    ),
    4: QuizQuestion('''A list of package\'s dependencies can be obtained from pip using its command named:''',
                    None,
                    None,
                    None,
                    {'A': 'deps', 'B': 'show', 'C': 'dir', 'D': 'list'},
                    ['B'],
                    ),
    5: QuizQuestion('''What is the expected value of the result variable after the following code is executed?''',
                    '''
                    import math  
                    result = math.e != math.pow(2, 4)  
                    print(int(result))''',
                    None,
                    None,
                    {'A': '0', 'B': '1', 'C': 'False', 'D': 'True'},
                    ['B'],
                    ),
    6: QuizQuestion('''The pip list command presents a list of:''',
                    None,
                    None,
                    None,
                    {'A': 'available pip commands', 'B': 'outdated local package',
                     'C': 'locally installed package', 'D': 'all packages available at PyPI'},
                    ['C'],
                    ),
    7: QuizQuestion('''How to use pip to remove an installed package?''',
                    None,
                    None,
                    None,
                    {'A': 'pip --uninstall package',
                     'B': 'pip remove package',
                     'C': 'pip install --uninstall package',
                     'D': 'pip uninstall package'},
                    ['D'],
                    ),
    8: QuizQuestion('''The following statement from a.b import c causes the import of:''',
                    None,
                    None,
                    None,
                    {'A': 'entity a from module b from package c', 'B': 'entity c from module a from package b',
                     'C': 'entity b from module a from package c', 'D': 'entity c from module b from package a'},
                    ['B'],
                    ),
    9: QuizQuestion('''The pyc file contains:''',
                    None,
                    None,
                    None,
                    {'A': 'a Python interpreter', 'B': 'compiled Python code',
                     'C': 'Python source code', 'D': 'a Python compiler'},
                    ['A'],
                    ),
    10: QuizQuestion('''A predefined Python variable that stores the current module name is called:''',
                     None,
                     None,
                     None,
                     {'A': '__name__', 'B': '__mod__', 'C': '__modname__', 'D': '__module__'},
                     ['A'],
                     ),
    11: QuizQuestion('''What is true about the pip search command? (Select three answers)''',
                     None,
                     None,
                     None,
                     {'A': 'all its searches are limited to locally installed packages',
                      'B': 'it needs working internet connection to work',
                      'C': 'it searches through all PyPI packages',
                      'D': 'it searches through package names only'},
                     ['A', 'B', 'C'],
                     ),
    12: QuizQuestion('''When a module is imported, its contents:''',
                     None,
                     None,
                     None,
                     {'A': 'are executed once (implicitly)',
                      'B': 'are ignored',
                      'C': 'are executed as many times as they are imported',
                      'D': 'may be executed (explicitly)'},
                     ['A'],
                     ),
    13: QuizQuestion('''Choose the true statements. (Select two answers)''',
                     None,
                     None,
                     None,
                     {
                         'A': 'The version function from the platform module returns a string with your Python version',
                         'B': 'The processor function from the platform module returns an integer with the number of processescurrently running in your OS',
                         'C': 'The version function from the platform module returns a string with your OS version',
                         'D': 'The system function from the platform module returns a string with your OS name'},
                     ['C', 'D'],
                     ),
    14: QuizQuestion('''What is true about the pip install command? (Select two answers)''',
                     None,
                     None,
                     None,
                     {'A': 'it allows the user to install a specific version of the package',
                      'B': 'it installs a package system-wide only when the --system option is specified',
                      'C': 'it installs a package per user only when the --user option is specified',
                      'D': 'it always installs the newest package version and it cannot be changed'},
                     ['A', 'C'],
                     ),
    15: QuizQuestion(
        '''Knowing that a function named fun() resides in a module named mod, and it has beenimported using the following line:''',
        '''import mod''',
        '''Choose the way it can be invoked in your code:''',
        None,
        {'A': 'mod->fun()', 'B': 'mod::fun()', 'C': 'mod.fun()', 'D': 'fun()'},
        ['C'],
    ),
    16: QuizQuestion('''The digraph written as #! is used to:''',
                     None,
                     None,
                     None,
                     {'A': 'tell a Unix or Unix-like OS how to execute the contents of a Python file',
                      'B': 'tell an MS Windows OS how to execute the contents of a Python file',
                      'C': 'create a docstring', 'D': 'make a particular module entity a private one'},
                     ['A'],
                     ),
    17: QuizQuestion('''A function which returns a list of all entities available in a module is called:''',
                     None,
                     None,
                     None,
                     {'A': 'entities()', 'B': 'content()', 'C': 'dir()', 'D': 'listmodule()'},
                     ['C'],
                     ),
    18: QuizQuestion('''What is true about updating already installed Python packages?''',
                     None,
                     None,
                     None,
                     {
                         'A': 'it can be done only by uninstalling and installing the package once again',
                         'B': 'it\'s an automatic process which doesn\'t require any user attention',
                         'C': 'it can be done by reinstalling the package using the reinstall command',
                         'D': 'it\'s performed by the install command accompanied by the -U option'},
                     ['D'],
                     )
}
