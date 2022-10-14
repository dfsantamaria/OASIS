from source.BehaviorManager import *

#test
#create a fresh ontology for the agent

ether_namespace = Namespace("http://www.dmi.unict.it/ether-oasis.owl#")
ontologyTemp=Graph()
ontologyTemp.load("ontologies/ether-oasis.owl")
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

agentinput1 = "http://www.dmi.unict.it/swb.owl#transferSWBWalletSource"
agentinput2 = "http://www.dmi.unict.it/swb.owl#transferSWBWalletDestination"
b.addClassAssertion(ontology, agentinput1, "EOA-EthereumAccount")
b.addClassAssertion(ontology, agentinput2, "EOA-EthereumAccount")
#mint behaviour
b.createAgentBehavior("mintSWBTokenBehaviour", "mintSWBGoal", "mintSWBTask",
                         ["mintSWBTaskOperator", "mint"],
                         ["mintSWBTaskOperatorArgument", "blockchain_digital_token"],
                         [
                             ["mintSWBTokenTaskObject", "refersAsNewTo", agentoutput1]
                         ],
                         [

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
                          ["transferSWBTokenInput1", "refersAsNewTo", agentoutput2],
                          ["transferSWBTokenInput2", "refersAsNewTo", agentinput1],
                          ["transferSWBTokenInput3", "refersAsNewTo", agentinput2]
                         ],
                         [
                            # ["transferSWBTokenOutput", "refersAsNewTo", agentoutput2]
                         ],
                         [
                          "transfer_ERC721_token_task_description",
                          [
                              ["transferSWBTokenTaskObject", "transfer_ERC721_token_task_object_template"]
                          ],
                          [
                              ["transferSWBTokenInput1", "transfer_ERC721_token_task_input_template_1"],
                              ["transferSWBTokenInput2", "transfer_ERC721_token_task_input_template_2"],
                              ["transferSWBTokenInput3", "transfer_ERC721_token_task_input_template_3"]
                          ],
                          [
                          ]
                         ])

#connect agent to agent behavior
b.connectAgentToBehavior("SWB_smart_contract_agent", "mintSWBTokenBehaviour")
b.connectAgentToBehavior("SWB_smart_contract_agent", "transferSWBTokenBehaviour")
executionObject="http://www.dmi.unict.it/swb.owl#swbtoken217"
#creating agent action
b.createAgentAction("SWB_smart_contract_agent", "mintToken217plan", "mintToken217Goal", "mintToken217Task",
                         ["mintToken217Operator", "mint"],
                         ["mintToken217Argument", "blockchain_digital_token"],
                         [
                             ["mintToken217Object", "refersExactlyTo", executionObject]
                         ],
                         [
                             #["executionInput1", "refersExactlyTo", executioninput1]
                         ],
                         [
                             ["mintToken217Output", "refersExactlyTo", executionObject]
                         ],
                         [
                          "mintSWBTask",
                          [
                              ["mintToken217Object", "transferSWBTokenTaskObject"]
                          ],
                          [
                              #["executionInput1", "MyAgentInput1"]
                          ],
                          [
                              ["mintToken217Output", "mintSWBTokenOutput"]
                          ]
                         ])


wallet1="http://www.dmi.unict.it/swb.owl#cp92producer"
wallet2="http://www.dmi.unict.it/swb.owl#cp132trader"
#creating agent action
b.createAgentAction("SWB_smart_contract_agent", "transferToken217plan-00", "transferToken217Goal-00", "transferToken217Task-00",
                         ["transferToken217Operator-00", "transfer"],
                         ["transferToken217Argument-00", "blockchain_digital_token"],
                         [
                             ["transferToken217Object-00", "refersExactlyTo", executionObject]
                         ],
                         [
                              ["transferToken217Input1-00", "refersExactlyTo", executionObject],
                              ["transferToken217Input2-00", "refersExactlyTo", wallet1],
                              ["transferToken217Input3-00", "refersAsNewTo", wallet2]
                         ],
                         [

                         ],
                         [
                          "transferSWBTask",
                          [
                              ["transferToken217Object-00", "transferSWBTokenTaskObject"]
                          ],
                          [
                              ["transferToken217Input1-00",  "transferSWBTokenInput1"],
                              ["transferToken217Input2-00",  "transferSWBTokenInput2"],
                              ["transferToken217Input3-00",  "transferSWBTokenInput3"]
                          ],
                          [

                          ]
                         ])


#serialization
#print("######################Agent################################")
#print(ontology.serialize(format="turtle"))

#Transfer activity
activity="http://www.dmi.unict.it/swb.owl#transferActivityToken217-00"
b.addClassAssertion(ontology, activity, "EthereumTokenFeatureModificationActivity")
b.addObjPropAssertion(ontology, activity, ether_namespace+"hasEthereumTokenFeatureModificationSource", namespace+"swbtoken217-pf-000")

b.addClassAssertion(ontology, namespace+"swbtoken217-pf-001", ether_namespace+"EthereumWalletOwnerPerdurantFeature")
b.addObjPropAssertion(ontology, namespace+"swbtoken217", ether_namespace+"hasEthereumTokenPerdurantFeature", namespace+"swbtoken217-pf-001")
b.addObjPropAssertion(ontology, namespace+"swbtoken217-pf-001", ether_namespace+"isInTheWalletOf", namespace+"cp132-trader")
b.addObjPropAssertion(ontology, activity, ether_namespace+"hasEthereumTokenFeatureModificationResult", namespace+"swbtoken217-pf-001")

#saving
file = open("ontologies/swb-example.owl", "w")
file.write(ontology.serialize(format='xml'))

