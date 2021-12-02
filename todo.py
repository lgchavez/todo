todo=['new york', 'california','washington state', 'italy', 'france', 'japan', 'brazil', 'spain', 'columbia', 'puerto rico', 'egypt']
#print(todo)
#print(len(todo))
#print(todo.index('columbia'))
#print("todo")
#for task in todo:
 # print(task)
print('where would you want to travel to?')
add = input()
todo.append(add)
remove = input()
todo.remove(remove)
todo.remove('washington state')
for task in todo:
  print(task)
