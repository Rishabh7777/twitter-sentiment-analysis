from ._anvil_designer import Form1Template
from anvil import *
import plotly.graph_objects as go
import anvil.server

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def categorise_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def categorise_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Call the google colab function and pass it the iris measurements
    count_list = anvil.server.call('predict_sentiment', self.text_box.text)
    # If a category is returned set our species
    if count_list == -1:
      self.no_user.visible = True
      self.no_user.text = "The twitter handle does not exist"
    elif count_list:
      self.plot_1.visible = True
      # Plot some data
      self.plot_1.data = [
        go.Scatter(
#           x = ['Positive', 'Negative', 'Neutral'],
#           y = [count_list[0], count_list[1], count_list[2]],
          marker = dict(
            color= 'rgb(16, 32, 77)'
          )
        ),
        go.Bar(
          x = ['Positive', 'Negative', 'Neutral'],
          y = [count_list[0], count_list[1], count_list[2]],
          name = 'Bar Chart Example'
        )
      ]
    else:
      self.no_user.visible = True
      self.no_user.text = "Something went wrong"

  def text_box_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

