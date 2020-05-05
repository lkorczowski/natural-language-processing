from louisnlp.utils.preprocessing import text_prepare



def test_text_prepare():
    examples = ["SQL Server - any equivalent of Excel's CHOOSE function?",
                "How to free c++ memory vector<int> * arr?"]
    answers = ["sql server equivalent excels choose function",
               "free c++ memory vectorint arr"]
    error_msg = []
    for ex, ans in zip(examples, answers):
        if text_prepare(ex) != ans:
            error_msg.append("Wrong answer for the case: '%s'" % ex)
    assert error_msg==[]