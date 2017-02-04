# - overview of virtualenv
# - virtualenv wrapper
# - https://docs.python.org/3/library/venv.html
# https://github.com/qw3rtman/p python version management

    # * Structuring python projects 
    # * Requirements.txt 
    # * Pydoc / Sphinx / Documentation 
    #     * docstrings 
    # * Debugging with pdb, PyCharm 
    #     * http://bash.org/?950581 
    #     * Find info about effective debugging 
    #     * https://medium.com/instamojo-matters/become-a-pdb-power-user-e3fc4e2774b2#.4m44e4qte 
    #     * https://codewords.recurse.com/issues/one/why-are-objects-so-hard-to-debug 


# ORGANIZE BELOW:
#
# * What Is Debugging? 
# * 
# * 1.3.1 Syntax Errors 
# * 1.3.2 Runtime Errors 
# * 1.3.3 Semantic Errors 
# * 1.3.4 Experimental Debugging 
# * 
#
#
#
#     * 	A simpler classification of bugs 2 types 
#
#
#
#
# Runtime bugs can be categorized along two dimensions:
#
# 1. 
# 2. Overt → covert: An overt bug has an obvious manifestation, e.g., the program crashes or takes far longer (maybe forever) to run than it should. A covert bug has no obvious manifestation. The program may run to conclusion with no problem—other than providing an incorrect answer. Many bugs fall between the two extremes, and whether or not the bug is overt can depend upon how carefully one examines the behavior of the program. 
# 3. 
# 4. 
# 5. Persistent → intermittent: A persistent bug occurs every time the program is run with the same inputs. An intermittent bug occurs only some of the time, even when the program is run on the same inputs and seemingly under the same conditions. When we get to Chapter 12, we will start writing programs of the kind where intermittent bugs are common. 
# 6. 
#
# The best kinds of bugs to have are overt and persistent. Developers can be under no illusion about the advisability of deploying the program. And if someone else is foolish enough to attempt to use it, they will quickly discover their folly. Perhaps the program will do something horrible before crashing, e.g., delete files, but at least the user will have reason to be worried (if not panicked). Good programmers try to write their programs in such a way that programming mistakes lead to bugs that are both overt and persistent. This is often called defensive programming.
#
#
#
#         * 
#         * 
#         * 
#         * 
#         * Debugging starts when testing has demonstrated that the program behaves in undesirable ways. Debugging is the process of searching for an explanation of that behavior. The key to being consistently good at debugging is being systematic in conducting that search. 
#         * 
#         * 
#         * 
#         * 
#         * 
#         * 
#         * 
#         * Think of debugging as a search process, and each experiment as an attempt to reduce the size of the search space. One way to reduce the size of the search space is to design an experiment that 
#         * 
#         * 
#         * 
#         * 
#         * 
#         * 
#         * Look for the usual suspects. E.g., have you 
#         * 
#         * o Passed arguments to a function in the wrong order, 
#         * 
#         * o Misspelled a name, e.g., typed a lowercase letter when you should have typed an uppercase one, 
#         * 
#         * o Failed to reinitialize a variable, 
#         * 
#         * o Tested that two floating point values are equal (==) instead of nearly equal (remember that floating point arithmetic is not the same as the arithmetic you learned in school), 
#         * 
#         * o Tested for value equality (e.g., compared two lists by writing the expression L1 == L2) when you meant object equality (e.g., id(L1) == id(L2)), 
#         * 
#         * o Forgotten that some built-in function has a side effect, 
#         * 
#         * 35 One might well wonder why there isn’t a static checker that detected the fact that the line of code temp.reverse doesn’t cause any useful computatation to be done, and is therefore likely to be an error. 
#         * 
#         * 36 He also reputedly told JFK, “Don't buy a single vote more than necessary. I'll be damned if I'm going to pay for a landslide.” 
#         * 
#         * 
#         * 
#         * 
#         * 
#         * 
#         * 
#         * 82 
#         * 
#         * 
#         * 
#         * Chapter 6. Testing and Debugging 
#         * 
#         * 
#         * 
#         * 
#         * 
#         * • 
#         * 
#         * • 
#         * 
#         * • 
#         * 
#         * • • • 
#         * 
#         * 
#         * 
#         * o Forgotten the () that turns a reference to an object of type function into a function invocation, 
#         * 
#         * o Created an unintentional alias, or 
#         * 
#         * o Made any other mistake that is typical for you. 
#         * 
#         * Stop asking yourself why the program isn’t doing what you want it to. Instead, ask yourself why it is doing what it is. That should be an easier question to answer, and will probably be a good first step in figuring out how to fix the program. 
#         * 
#         * Keep in mind that the bug is probably not where you think it is. If it were, you would probably have found it long ago. One practical way to go about deciding where to look is asking where the bug cannot be. As Sherlock Holmes said, “Eliminate all other factors, and the one which remains must be the truth.”37 
#         * 
#         * Try to explain the problem to somebody else. We all develop blind spots. It is often the case that merely attempting to explain the problem to someone will lead you to see things you have missed. A good thing to try to explain is why the bug cannot be in certain places. 
#         * 
#         * Don’t believe everything you read. In particular, don’t believe the documentation. The code may not be doing what the comments suggest. 
#         * 
#         * Stop debugging and start writing documentation. This will help you approach the problem from a different perspective. 
#         * 
#         * Walk away, and try again tomorrow. This may mean that bug is fixed later in time than if you had stuck with it, but you will probably spend a lot less of your time looking for it. That is, it is possible to trade latency for efficiency. (Students, this is an excellent reason to start work on programming problem sets earlier rather than later!) 
#
# One-liner: python -c 'command' • Debugger: python -m pdb file.py
