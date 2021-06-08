import components
import pandas as pd

N_GPU = pd.read_csv('NvidiaGraphicsCard.csv')
A_GPU = pd.read_csv('AMDGraphicsCard.csv')
A_CPU = pd.read_csv('AMDProcessor.csv')
I_CPU = pd.read_csv('IntelProcessor.csv')

print("Action List:\n"
      "make build\n"
      "check builds\n"
      "compare\n")

def check_action():
      action = input("What do you want to do?: ")
      return action

def build():
      c_brand = input("Which brand of CPU do you want?: "
                      "(Intel, AMD)")
      if c_brand == "Intel" :
            c_list = I_CPU['Name']
            for i in range(len(c_list)):
                  print(c_list[i])
      else :
            c_list = A_CPU['Name']
            for i in range(len(c_list)):
                  print(c_list[i])

      cpu = input("which CPU would you like to use?: ")
      mem = input("How much gigabytes of RAM would you like to use?: ")
      g_brand = input("Which brand of Graphics Card do you want?: "
                      "(AMD, Nvidia)")
      if g_brand == "AMD" :
            g_list = A_GPU['Name']
            for i in range(len(g_list)):
                  print(g_list[i])
      else :
            g_list = N_GPU['Name']
            for i in range(len(g_list)):
                  print(g_list[i])
      gpu = input("Which Graphics Card would you like to use?: ")
      return [c_brand, cpu, mem, g_brand, gpu]

def compare(builds):
      demand = input("What is the purpose of the build?: "
                     "(gaming, video editing, rendering)")
      point = []
      cp = []
      rank = []
      if demand == 'gaming':
            for i in range(len(builds)):
                if builds[i][0] == 'Intel':
                      cpu_spec = I_CPU.loc[I_CPU['Name'] == builds[i][1]]
                      cpu_score = cpu_spec[['Single']].iloc[0][0]
                      cpu_score = cpu_score * 4
                      cpu_price = cpu_spec[['MSRP']].iloc[0][0]
                else :
                      cpu_spec = A_CPU.loc[A_CPU['Name'] == builds[i][1]]
                      cpu_score = cpu_spec[['Single']].iloc[0][0]
                      cpu_score = cpu_score * 4
                      cpu_price = cpu_spec[['MSRP']].iloc[0][0]
                if builds[i][3] == 'AMD':
                      gpu_spec = A_GPU.loc[A_GPU['Name'] == builds[i][4]]
                      gpu_score = gpu_spec[['Passmark']].iloc[0][0]
                      gpu_price = gpu_spec[['MSRP']].iloc[0][0]
                else:
                      gpu_spec = N_GPU.loc[N_GPU['Name'] == builds[i][4]]
                      gpu_score = gpu_spec[['Passmark']].iloc[0][0]
                      gpu_price = gpu_spec[['MSRP']].iloc[0][0]

                build_score = cpu_score + gpu_score
                build_price = cpu_price + gpu_price
                point.append(build_score)
                cp.append(build_score/build_price)
            best = point.index(max(point))
            print("The most powerful build is No." + str(best) + " build!")
            budget =  cp.index(max(cp))
            print("The most high value build is No." + str(budget) + " build!")
      else:
            for i in range(len(builds)):
                if builds[i][0] == 'Intel':
                      cpu_spec = I_CPU.loc[I_CPU['Name'] == builds[i][1]]
                      cpu_score = cpu_spec[['Multi']].iloc[0][0]
                      cpu_score = cpu_score * 2
                      cpu_price = cpu_spec[['MSRP']].iloc[0][0]
                else :
                      cpu_spec = A_CPU.loc[A_CPU['Name'] == builds[i][1]]
                      cpu_score = cpu_spec[['Multi']].iloc[0][0]
                      cpu_score = cpu_score * 2
                      cpu_price = cpu_spec[['MSRP']].iloc[0][0]
                if builds[i][3] == 'AMD':
                      gpu_spec = A_GPU.loc[A_GPU['Name'] == builds[i][4]]
                      gpu_score = gpu_spec[['Passmark']].iloc[0][0]
                      gpu_price = gpu_spec[['MSRP']].iloc[0][0]
                else:
                      gpu_spec = N_GPU.loc[N_GPU['Name'] == builds[i][4]]
                      gpu_score = gpu_spec[['Passmark']].iloc[0][0]
                      gpu_price = gpu_spec[['MSRP']].iloc[0][0]

                build_score = cpu_score + gpu_score
                build_price = cpu_price + gpu_price
                point.append(build_score)
                cp.append(build_score/build_price)
            best = point.index(max(point))
            print("The most powerful build is No." + str(best) + " build!")
            budget =  cp.index(max(cp))
            print("The most high value build is No." + str(budget) + " build!")
      print(point)



build_list = [['AMD', '5900x', '16', 'AMD', '6900XT'],
              ['Intel', '11600k', '16', 'AMD', '6800XT'],
              ['AMD', '5600x', '16', 'AMD', '6700XT']]
while True:
      todo = check_action()
      if todo == 'make build':
            build_list.append(build())
      elif todo == 'check builds':
            print(build_list)
      elif todo == 'compare':
            compare(build_list)
      else :
            print('Invalid Action')





