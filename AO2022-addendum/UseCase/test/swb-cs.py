from source.BehaviorManager import *

#test
#create a fresh ontology for the agent

ether_namespace = Namespace("http://www.dmi.unict.it/ether-oasis.owl#")
ontologyTemp=Graph()
ontologyTemp.load("ontologies/ether.owl")
ontologyTemp.bind("base", ether_namespace)

namespace =  Namespace("http://www.dmi.unict.it/swb.owl#")
ontology=Graph()
ontology.parse("ontologies/swb-cs.owl")
ontology.bind("base", namespace)

# Create the graph
b = BehaviorManager(ontology, namespace, None,
                    ontologyTemp, ether_namespace, None,
                    ontology, namespace, None,
                    ontology, namespace, None)


#Crate agent
b.createAgent("SWB_smart_contract_agent")

#create agent behaviour
agentoutput1 = "http://www.dmi.unict.it/swb.owl#mintSWBTokenType"
agentoutput2 = "http://www.dmi.unict.it/swb.owl#transferSWBTokenType"
b.addClassAssertion(ontology, agentoutput1, "SWBWheatToken")
b.addClassAssertion(ontology, agentoutput2, "SWBWheatToken")

#mint behaviour
b.createAgentBehavior("mintSWBTokenBehaviour", "mintSWBGoal", "mintSWBTask",
                         ["mintSWBTaskOperator", "mint"],
                         ["mintSWBTaskOperatorArgument", "blockchain_digital_token"],
                         [
                             ["mintSWBTokenTaskObject", "refersAsNewTo", agentoutput1]
                         ],
                         [
                             #["MyAgentInput1", "refersAsNewTo", agentinput1]
                         ],
                         [
                             ["mintSWBTokenOutput", "refersAsNewTo", agentoutput1]
                         ],
                         [
                          "mint_ERC721_token_task_description",
                          [
                              ["mintSWBTokenTaskObject", "mint_ERC721_token_task_object_template"]
                          ],
                          [
                              #["MyAgentInput1", "MyTemplateInput1"]
                          ],
                          [
                              ["mintSWBTokenOutput", "mint_ERC721_token_task_object_template"]
                          ]
                         ])

#transfer behaviour
b.createAgentBehavior("transferSWBTokenBehaviour", "transferSWBGoal", "transferSWBTask",
                         ["transferSWBTaskOperator", "transfer"],
                         ["transferSWBTaskOperatorArgument", "blockchain_digital_token"],
                         [
                             ["transferSWBTokenTaskObject", "refersAsNewTo", agentoutput2]
                         ],
                         [
                             ["transferSWBTokenInput", "refersAsNewTo", agentoutput2]
                         ],
                         [
                             ["transferSWBTokenOutput", "refersAsNewTo", agentoutput2]
                         ],
                         [
                          "transfer_ERC721_token_task_description",
                          [
                              ["transferSWBTokenTaskObject", "transfer_ERC721_token_task_object_template"]
                          ],
                          [
                              ["transferSWBTokenInput", "transfer_ERC721_token_task_input_template_1"]
                          ],
                          [
                              ["transferSWBTokenOutput", "transfer_ERC721_token_task_object_template"]
                          ]
                         ])

#connect agent to agent behavior
b.connectAgentToBehavior("SWB_smart_contract_agent", "mintSWBTokenBehaviour")
b.connectAgentToBehavior("SWB_smart_contract_agent", "transferSWBTokenBehaviour")



#serialization
#print("######################Agent################################")
#print(ontology.serialize(format="turtle"))





#saving
file = open("ontologies/swb-cs2.owl", "w")
file.write(ontology.serialize(format='xml'))

