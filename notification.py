from toaster import toaster

# define the xml notification document.
tString = """
<toast launch="alarmLaucnhArg" scenario="alarm">
  <visual>
    <binding template="ToastGeneric">
      <text>Good morning!</text>
      <text>7 + 15 = ?</text>
    </binding>
  </visual>
  <actions>
    <action activationType="system" arguments="snooze" content="" />
    <action activationType="background" arguments="dismiss" content="Dismiss" />
  </actions>
</toast>
"""

# load the xml document.
xDoc = dom.XmlDocument()
xDoc.load_xml(tString)
notification = notifications.ToastNotification(xDoc)

# display notification
notifier.show(notification)