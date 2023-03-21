
### STACK in PYTHON ###
### LIFO - Last in, First out ###

from typing import List, Any
from copy import deepcopy

class Stack:
    def __init__(self):
        # Stack genérica podendo receber qualquer tipo de dados
        self.__data: List[Any] = []
        # Índice para iteraçoes
        self.__index = 0

    def append(self, item: Any) -> None:
        "Append da lista"
        self.__data.append(item)
    
    def pop(self) -> Any:
        "Pop da lista"
        if not self.__data:
            return
        return self.__data.pop()

    def peek(self) -> Any:
        "Retorna o último elemento da lista"
        if not self.__data:
            return
        return self.__data[-1]
    
    def __repr__(self) -> str:
        "Representando os dados"
        return str(self.__data)
    
    def __iter__(self):
        "Setar index para Iteração com for"
        self.__index = len(self.__data)
        return self

    def __next__(self):
        "Para iteração com for (next item)"
        if self.__index == 0:
            raise StopIteration
        self.__index -= 1
        return self.__data[self.__index]

    def __bool__(self):
        "Iteração com While"
        return bool(self.__data)

if __name__ == "__main__":
    stack = Stack()

    stack.append("Teste1")
    stack.append("Teste2")
    stack.append("Teste3")

    print("Original Stack: ")
    print(stack)
    print("-"*30, '\n')

    print("For: ")
    for i in stack:
        print(i)
    print("-"*30, '\n')

    print("Pop:")
    last_item = stack.pop()
    print(stack, last_item)
    print("-"*30, '\n')

    print("While: ")
    stack_copy = deepcopy(stack)
    while stack_copy:
        print(stack_copy.pop())
