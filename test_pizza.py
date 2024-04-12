import pytest
import random
import assessMeTester_StringSimilarity
#TO RUN pytest --tb=short -s

import pizza_pizza

def test_pizza_class(capsys, monkeypatch, printFeedback=True):
        success = True
        assertMessage = "" ##Assert message

        ##MODIFY
        testerName = "test_pizza_class"
        className = "class Pizza"

          
        try:

            # invoke
            pizza = pizza_pizza.Pizza()
            
            ##check the default attributes
            attributesOk = True

            #Before any attribute test, put assert message if 
            assertMessage="Attribute error: price\n"
            if pizza.price != 5.0:
                attributesOk=False
            assertMessage="Attribute error: veggies\n"
            if len(pizza.veggies) != 0:
                attributesOk=False
            if type(pizza.veggies) != set:
                attributesOk=False
            assertMessage="Attribute error: meats\n"
            if len(pizza.meats) != 0:
                attributesOk=False
            if type(pizza.meats) != set:
                attributesOk=False
            assertMessage="Attribute error: cheese\n"
            if pizza.cheese != 's':
                attributesOk=False
            assertMessage=""
            # Part for string comparison!
            if attributesOk==True:
                
                assert True
            else:
                success = False
                assertMessage=f"The {className} is not correct!\n"
                assertMessage = f"The defaut value or attribute types are not properly defined!"
        except AttributeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except TypeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except AssertionError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except:
            pass
        
        feedback = "\n\033[91m" ## RED START
        feedback = feedback + "\n******************************************* "+testerName+ " *****************\n"
        feedback = feedback + "\033[93m"+ assertMessage+"\033[0m"+"\n\n"
        feedback = feedback + "\n\033[91m*******************************************************************************\n"
        feedback = feedback + "\033[0m" ## RED END
        feedback = feedback + "\n\n\n"

        if printFeedback and len(assertMessage)>0:
            print(feedback)
        assert success,assertMessage



def test_topping_class(capsys, monkeypatch, printFeedback=True):
        success = True
        assertMessage = "" ##Assert message

        ##MODIFY
        testerName = "test_topping_class"
        className = "class Topping"

          
        try:

            # invoke
            topping = pizza_pizza.Topping('p', 'Pepperoni', 1.5)
            
            ##check the default attributes
            attributesOk = True

            #Before any attribute test, put assert message if 
            assertMessage="Attribute error: code\n"
            if topping.code != 'p':
                attributesOk=False
            assertMessage="Attribute error: name\n"
            if topping.name != "Pepperoni":
                attributesOk=False
            assertMessage="Attribute error: price\n"
            if topping.price != 1.5:
                attributesOk=False
            assertMessage=""
            # Part for string comparison!
            if attributesOk==True:
                
                assert True
            else:
                success = False
                assertMessage=f"The {className} is not correct!\n"
                assertMessage = f"The defaut value are not properly defined!"
        except AttributeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except TypeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except AssertionError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except:
            pass
        
        feedback = "\n\033[91m" ## RED START
        feedback = feedback + "\n******************************************* "+testerName+ " *****************\n"
        feedback = feedback + "\033[93m"+ assertMessage+"\033[0m"+"\n\n"
        feedback = feedback + "\n\033[91m*******************************************************************************\n"
        feedback = feedback + "\033[0m" ## RED END
        feedback = feedback + "\n\n\n"

        if printFeedback and len(assertMessage)>0:
            print(feedback)
        assert success,assertMessage



def test_print_pizza(capsys, monkeypatch, printFeedback=True):

        
    expected_output1 = """One pizza with Cheddar, Bacon, Bell Peppers, Mushrooms,  : $5.0"""


    expected_output2 = """One pizza with Cheddar, Bacon, Mushrooms, Bell Peppers,  : $5.0"""

    
    # Execute the function
      # Run the main function
    pizza1 = pizza_pizza.Pizza()
    pizza1.cheese='c'
    pizza1.meats.add(pizza_pizza._MEATS['b'])
    pizza1.veggies.add(pizza_pizza._VEGGIES['m'])
    pizza1.veggies.add(pizza_pizza._VEGGIES['b'])
    pizza_pizza.print_pizza(pizza1)
    #Get the feedback
    captured = capsys.readouterr()

    similarity_threshold = 0.99  # Set your desired threshold here

    similarity_score1 = assessMeTester_StringSimilarity.string_similarity(expected_output1, captured.out)
    similarity_score2 = assessMeTester_StringSimilarity.string_similarity(expected_output2, captured.out)

   
    if similarity_score1 >= similarity_threshold or similarity_score2>=similarity_threshold: 
        feedback = "Strings are similar enough (score: {0:.2f}%). Test passed!".format(max(similarity_score1,similarity_score2) * 100)
    else:
        feedback = "\n\033[91m" ## RED START
        feedback = feedback + "***************test_print_pizza tester failed!***************"
        feedback = feedback+ "\nExpected:\n" +"\033[93m"+ expected_output1+"\033[0m"+"\n\n"
        feedback = feedback + "\nCaptured:\n" +"\033[93m"+  captured.out +"\033[0m"
        feedback = feedback+ "\n\033[91m" ## RED START
        feedback = feedback + f"Strings are not similar enough (score: {similarity_score1})"
        feedback = feedback + "\n***********************************************************\n"
        feedback = feedback + "\033[0m" ## RED END
    # Use sys.stdout to write out the feedback message
    if(printFeedback):
        print(feedback + "\n")
  

    assert similarity_score1 >= similarity_threshold or similarity_score2>=similarity_threshold, f"Strings are not similar enough (score: {similarity_score1})"


def test_category_class(capsys, monkeypatch, printFeedback=True):
        success = True
        assertMessage = "" ##Assert message

        ##MODIFY
        testerName = "test_category_class"
        className = "class Category"

          
        try:

            # invoke
            veggiesCategory = pizza_pizza.Category (pizza_pizza._VEGGIES, "Veggie")
            
            ##check the default attributes
            attributesOk = True

            #Before any attribute test, put assert message if 
            
            assertMessage="Attribute error: code\n"
            if type(veggiesCategory.category) != dict:
                attributesOk=False
            assertMessage="Attribute error: name\n"
            if veggiesCategory.name != "Veggie":
                attributesOk=False
            # Part for string comparison!
            assertMessage=""
            if attributesOk==True:
                assert True
            else:
                success = False
                assertMessage=f"The {className} is not correct!\n"
                assertMessage = f"The defaut value are not properly defined!"
        except AttributeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except TypeError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except AssertionError as e:
             success=False
             assertMessage +="ErrorFeedback:" + str(e)
        except:
            pass
        
        feedback = "\n\033[91m" ## RED START
        feedback = feedback + "\n******************************************* "+testerName+ " *****************\n"
        feedback = feedback + "\033[93m"+ assertMessage+"\033[0m"+"\n\n"
        feedback = feedback + "\n\033[91m*******************************************************************************\n"
        feedback = feedback + "\033[0m" ## RED END
        feedback = feedback + "\n\n\n"

        if printFeedback and len(assertMessage)>0:
            print(feedback)
        assert success,assertMessage
