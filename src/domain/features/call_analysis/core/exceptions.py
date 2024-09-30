class CallNotFoundException(Exception):
    
    def __init__(self, call_id: str) -> None:
        super().__init__(f"Call with id '{call_id}' not found.")
