
tasks = []


is_running = True
# todays_tasks = input(f"My today's schedule: ")
print(f"What are you going to do today? (Type 'exit' to stop adding tasks)")
i = 1
while is_running:
    todays_tasks = input("")
    i = i+1

    if(todays_tasks.lower() == "exit"):
        is_running = False
    else:
        tasks.append(todays_tasks)

print(f"My today's schedule: ")
for j, taskss in enumerate(tasks,  start=1):
    print(f"{j}. {taskss}")
   







