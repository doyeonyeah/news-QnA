## Form1
# Site layout

from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def ask_button_click(self, **event_args):
    question = self.question.text
    topic = self.topic.text
    when = self.when.text
    num = self.num_articles.text
    top_k = self.top_k.text
    
    self.show_status.text = "Loading..."
    self.repeating_panel.items = None
    
    results = anvil.server.call("ask_qna", topic, question, when, num, top_k)
    
    self.show_status.text = question
    self.repeating_panel.items = results

# TopResults
# Display top results

from ._anvil_designer import TopResultsTemplate
from anvil import *
import anvil.server


class TopResults(TopResultsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    if self.item is None:
      self.repeat_answer.text = ""
      self.repeat_additional.text = ""
    else:
      self.repeat_answer.text = str(self.item['numbering'])+". "+ self.item['answer']
      self.repeat_answer.url = self.item['url']
      self.repeat_additional.text = "Likelihood: " + str(round(self.item['score'], 4))
      
