web = {
    'header':'header.html',
    'footer':'footer.html',
    'content': ''
}


def readfile(filename:str):
    
    """[read the file takes in filename]

    Returns:
        [type]: [description]
    """
    with open(filename,"r") as file_handle:
        file_contents = file_handle.read()
        
        return file_contents
    
    
    
def create_index(filename:str, filecontent:str):
    with open(filename, "w") as file_handle:
        file_handle.write(filecontent)


import pandas as pd
import random as r

data = {
    'x':list(range(1,11)),
    'y':[r.randint(1,100) for i in range(1,11)]
}

df = pd.DataFrame(data)

header_content = readfile(web['header'])
footer_content = readfile(web['footer'])
web['content'] = df.to_html( index = False, table_id ='sales')
index_content = header_content + web['content'] + footer_content
create_index('index.html', index_content)


