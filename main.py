from fastmcp import FastMCP
import random
import json
mcp=FastMCP("simple calculator")

@mcp.tool
def add(a:int,b:int)->int:
    """add two number"""
    return a+b

@mcp.tool
def random_number(min_val:float=1,max_val:float=100)->float:
    """generate a number between min and max value"""
    return random.randint(min_val,max_val)

@mcp.resource("info://servers")
def server_info()->str:
    """get information about the server"""
    info={
        "name":"simple calculator server",
        "version":"1.0.0",
        "description":"a basic mcp server with math tool",
        "tools":["add","random_number"],
        "author":"your name"
    }
    return json.dumps(info,indent=2)
if __name__=="__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)
    
