import sys

class arg:
    def reset_list(self):
        self.arg_list={
        "args":[],
        "options":[]
        }

    def __init__(self):
        self.reset_list()

    def def_type(self,x,param):
        result={
            "type":"data",
            "src":x
        }
        if(x[:1]=='-'):
            result["type"]="option"
            if(param["case-sensitive"]):
                result["value"]=x
            else:               
                result["value"]=x.lower()
        else:
            if param["list"]:
                result["type"]="list"
                result["value"]=x.split(param["list_by"])
            else:
                result["type"]="data"
                result["value"]=x                    
        return result

    def read_arg(self,*param_):
        param={
            "case-sensitive":True,
            "list":False,
            "list_by":":",
            "args":""
        }
        if(len(param_)==1):
            for key,value in param_[0].items():
                if(key in param):
                    param[key]=value
        self.reset_list()
        if(param["args"]!=""):
            argv=[]
            j=param["args"].split(" ")
            for x in j:
                s1=x.strip()
                if(s1!=""):
                    argv.append(s1)
        else:
            argv=sys.argv
        for x in argv:
            h=self.def_type(x,param)
            if h["type"]=="option":
                if not (h["value"] in self.arg_list["options"]):
                    self.arg_list["options"].append(h["value"])
            self.arg_list["args"].append(h)
        return self.arg_list

# arg_list={
#     "args":[],
#     "options":[]
#     }

# def def_type(x,param):
#     result={
#         "type":"data",
#         "src":x
#     }
#     if(x[:1]=='-'):
#         result["type"]="option"
#         if("case_sensetive" in param):
#             result["value"]=x
#         else:
#             result["value"]=x.lower()
#     else:
#         if("list" in param):
#             if param["list"]:
#                 if "list_by" in param:
#                     ch=param["list_by"]
#                 else:
#                     ch=":"
#                 result["type"]="list"
#                 result["value"]=x.split(ch)
#             else:
#                 result["type"]="data"
#                 result["value"]=x                    
#         else:
#             result["type"]="data"
#             result["value"]=x
#     return result

# def read_arg(param={}):
#     global arg_list
#     arg_list={
#         "args":[],
#         "options":[]
#     }
#     if("args" in param):
#         argv=[]
#         j=param["args"].split(" ")
#         for x in j:
#             s1=x.strip()
#             if(s1!=""):
#                 argv.append(s1)
#     else:
#         argv=sys.argv
#     for x in argv:
#         h=def_type(x,param)
#         if h["type"]=="option":
#             if not (h["value"] in arg_list["options"]):
#                 arg_list["options"].append(h["value"])
#         arg_list["args"].append(h)
#     return arg_list

# print(read_arg(param={"args":"prg -x  -y z 123.txt 2345.txt"}))

