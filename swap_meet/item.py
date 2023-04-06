import uuid
import n2w

class Item:
    def __init__(self, id=None, condition=0):
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition
    
    def get_category(self):
        return type(self).__name__
    
    def __str__(self):
        return f'An object of type {self.get_category()} with id {self.id}.'
    
    def condition_description(self):
        '''Imported n2w module: number to word, 
        that converts given integer to the string/word version of it.'''
        
        if isinstance(self.condition, int):
            description = (
                f'{n2w.convert(self.condition).capitalize()} green bottles\n' 
        'Hanging on the wall\n'
        f'{n2w.convert(self.condition).capitalize()} green bottles\n'
        'Hanging on the wall\n'
        'And if one green bottle\n'
        'Should accidentally fall\n'
        f'There will be {n2w.convert(self.condition - 1)} green bottles\n'
        'Hanging on the wall.'
        )  
        else:
            description = (
                f'{self.condition} green bottles\n' 
        'Hanging on the wall\n'
        f'{self.condition} green bottles\n'
        'Hanging on the wall\n'
        'And if one green bottle\n'
        'Should accidentally fall\n'
        f'There will be {self.condition - 1} green bottles\n'
        'Hanging on the wall.'
        )
            
        return description