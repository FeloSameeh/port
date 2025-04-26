import queue

class EventTrigger:
    def _init_(self):
        self.event_queue = queue.Queue()

    def trigger_event(self, event):
        print(f"Event Detected: {event}")
        if event == "DDoS Attack Detected":
            self.add_event("Updating Firewall")

    def add_event(self, new_event):
        self.event_queue.put(new_event)
        print(f"Added to Queue: {new_event}")

    def process_events(self):
        while not self.event_queue.empty():
            event = self.event_queue.get()
            print(f"Processing: {event}")


event_system = EventTrigger()
event_system.trigger_event("DDoS Attack Detected")
event_system.process_events()