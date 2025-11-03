import json

with open("ITS_Python/Recupero/esame_recupero/info.json") as file:
    dict_task: dict[str, dict[str, str|bool]]  = json.load(file)


class TaskManager:

    tasks: dict[str, dict[str, str|bool]]

    def __init__(self, tasks: dict[str, dict[str, str|bool]] = {}) -> None:

        self.tasks: dict[str, dict[str, str|bool]] = tasks


    def create_task(self, task_id:str, descrizione: str) -> dict[str, dict[str, str|bool]]|str:
        if task_id in self.tasks:
            raise KeyError("Il task_id esiste gia")
        else:
            temp_dict: dict[str, str|bool] = {
                "descrizione": descrizione,
                "completato": False
            } 
        self.tasks[task_id] = temp_dict
        return {task_id: temp_dict}
    
    def complete_task(self, task_id:str) -> dict[str, dict[str, str|bool]]|str:
        if task_id not in self.tasks:
            raise KeyError("L'errore, il task_id non esiste")
        else:
            self.tasks[task_id]["completato"] = True
            return {task_id: self.tasks[task_id]}
        
    def update_description(self, task_id:str, nuova_descrizione:str) -> dict | str:
        if task_id not in self.tasks:
            raise KeyError("Task non è presente")
        else:
            self.tasks[task_id]["decrizione"] = nuova_descrizione
            return {task_id: self.tasks[task_id]}
        
    def remove_task(self, task_id:str) -> dict|str:
        if task_id not in self.tasks:
            raise KeyError("Il task non esiste")
        else:
            value = self.tasks.pop(task_id)
            #key, value = self.tasks.popitem(task_id)
            return {task_id: value}
        
    def list_tasks(self) -> list[str]:
            
        return list(self.tasks.keys())
    
    def get_task(self, task_id:str) -> dict | str:
        if task_id not in self.tasks:
            raise KeyError
        else:
            return self.tasks[task_id]

        
    



task_manager_1: TaskManager = TaskManager(dict_task)

