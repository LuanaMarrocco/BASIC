#!/usr/bin/env python
import docker
import re

class DockerEnvCar:

    #client = docker.DockerClient(base_url='tcp://192.168.99.100:2375 /')
    client = docker.from_env()
    container = None
    RobotID = None
    smartContractAddress = None
    
    
    def __init__(self, RobotId):
        self.RobotID = RobotId
        self.getContainer()
        response = self.exec_deploy()
        print(response)
        self.smartContractAddress = self.extract_contract_address(response)
                                  
    def getContainer(self):
        DockerComposerID = int(self.RobotID) + 1
        self.container = self.client.containers.get("docker-geth-network-master_eth_"\
                                                    + str(DockerComposerID))
        
    def exec_deploy(self):
    	# self.makeMiningWhenPendingTransactionOnly()
        print("Deploying the car " + str(self.RobotID))
        response = self.container.exec_run("node /root/js/deploy.js /root/smart_contracts/smart_contract_askingCar.sol " + str(self.RobotID))
        return response
        
    def check(self):
        print (self.client.containers.list())

    def extract_contract_address(self, string):
        string = str(string)
        list = string.split("contractAddress: '")
        addressList = list[1].split("'")
        address = addressList[0]
        return address
    
    def getContractAddress(self):
        return self.smartContractAddress
        


