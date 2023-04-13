import time

JS_ADD_TEXT_TO_INPUT = """
  let element = arguments[0], txt = arguments[1];
  element.value += txt;
  element.dispatchEvent(new Event('change'));
  """

def input_type(driver, element, text):
    print('TYPING: ' + text)
    driver.execute_script(JS_ADD_TEXT_TO_INPUT, element, text)
    time.sleep(1)