from ast import Return, arg
from asyncio import tasks
import cmd
import os
import json
from tkinter import NO
from datetime import datetime

json_output = 'Tasks.json'

class CLI(cmd.Cmd):
    prompt = 'task-cli > '

    intro = ' Welcome to my CLI for TasckTracker. Type "help" for avaliable commands.'
    
    def __init__(self):
        super().__init__()
        self.tasks = self.load_tasks() #cargar tareas existentes

    def load_tasks(self):
        if os.path.exists(json_output):
            with open(json_output, 'r', encoding='utf-8') as json_file:
                try:
                    return json.load(json_file)
                except json.JSONDecodeError as e:
                     return []  # Si el archivo está vacío o mal formado, empezar con una lista vacía
        return []

    def do_add(self, line):
        """
        This method append a new task in te list
        """

        last_task = None

        last_task_id = 0
        try:

            if self.tasks:

                last_task = self.tasks[-1] #Acees the last item
                        
                last_task_id = int(last_task['task_id']) + 1 
            else:
                print("No tasks here")

        except Exception as e:
            print(f"Error al acceder al ultimo elemento: {e}")

        try:
            
            new_task = {
                'task_id' :last_task_id,
                'task_description' : line,
                'task_status' : ' ',
                'task_createdAT' : str(datetime.now()),
                'task_updatedAT' : ' '
            }

            self.tasks.append(new_task)
            
            #Generate a json file with new tasks
            with open(json_output, 'w', encoding='utf-8') as json_file:

                json.dump(self.tasks, json_file, ensure_ascii=False, indent=4)

            print(f'Task added successfully (ID: {last_task_id})')

        except Exception as e:
            print (f'task no add {e}')
        #add new task

    def do_list(self, line):
        """ List all the tasks """
        
        for task in self.tasks:
            print(f' Task: {task['task_id']}')
            print(f' Description: {task['task_description']}')
            print(f' Status: {task['task_status']}')
            print(f' Created at: {task['task_createdAT']}')
            print(f' Last update: {task['task_updatedAT']}\n')

    def do_delete(self, line):
        
        saved_tasks = []
        
        for task in self.tasks:
            
            if task['task_id'] != int(line):
                
                saved_tasks.append(task)
               

        with open(json_output, 'w', encoding='utf-8') as json_file:
            json.dump(saved_tasks, json_file, ensure_ascii=False, indent=4)
        print(f"Task {line} deleted successfully.")
        self.tasks = saved_tasks
    
    # Searcha a task by id
    def do_search(self, line):
        """This metohd search a task by id"""
        for task in self.tasks:
            if task['task_id'] == int(line):
                print(f'\nTask: {task["task_id"]}')
                print(f'Description: {task["task_description"]}')
                print(f'Status: {task["task_status"]}')
                print(f'Created at: {task["task_createdAT"]}')
                print(f'Last update: {task["task_updatedAT"]}')
                break
        else:
            print(f"Task {line} not found")
        
    def do_update(self, line):
        
        line_split = line.split(" ", 1)

        try:
            id = int(line_split[0])

        except Exception as e:
            print(f"Id error: {e}")
        


        for task in self.tasks:
            if task['task_id'] == id:
                
                task['task_description'] = line_split[1]
                task['task_updatedAT'] = str(datetime.now())
                
                break
        
        self.tasks = self.tasks
            
        #Generate a json file with new tasks
        with open(json_output, 'w', encoding='utf-8') as json_file:

            json.dump(self.tasks, json_file, ensure_ascii=False, indent=4)

        print(f'Task updated successfully (ID: {id})')

    """
    def do_mark_in_progresss(self, line):
        try:
        
            status = int(line)
                
            for task in self.tasks:
                if task['task_id'] == id:
                
                    task['task_status'] = status

                    break
            
            self.tasks = self.tasks

            with open(json_output, 'w', encoding='utf-8') as json_file:

                json.dump(self.tasks, json_file, ensure_ascii=False, indent=4)

            print(f'Status updated successfully for (ID: {id})')

        except Exception as e:
            print(f"Status error: {e}")

    """

    def mark_done(parameter_list):
        """
        docstring
        """
        pass

    def do_quit(self, line):
        """Exit the CLI."""
        return True
    

if __name__ == '__main__':
    CLI().cmdloop()