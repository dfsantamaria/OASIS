from BehaviorManager import *

#test
#create a fresh ontology for the agent
namespace =  Namespace("http://www.test.org/myOntology#")
ontology=Graph()
ontology.namespace_manager.bind("base", namespace)


#create a fresh ontology for the agent template
namespaceTemp =  Namespace("http://www.test.org/myOntologyTemplate#")
ontologyTemp=Graph()
ontologyTemp.namespace_manager.bind("base", namespaceTemp)

#create a fresh ontology for the agent actions
namespaceAct = Namespace("http://www.test.org/myOntologyActions#")
ontologyAct=Graph()
ontologyAct.namespace_manager.bind("base", namespaceAct)

#create a fresh ontology for the agent plan
namespacePlan = Namespace("http://www.test.org/myOntologyPlans#")
ontologyPlan=Graph()
ontologyPlan.namespace_manager.bind("base", namespacePlan)

# Create the graph
b = BehaviorManager(ontology, namespace, None,
                    ontologyTemp, namespaceTemp, None,
                    ontologyAct, namespaceAct, None,
                    ontologyPlan, namespacePlan, None)


#create agent template
agentTemplateName=b.createAgentTemplate("MyAgentBehaviorTemplate")
#create behavior template
object1 = "http://www.test.org/myOntologyTemplate#template-object-entity-1"
input1 = "http://www.test.org/myOntologyTemplate#template-input-entity-1"
output1 = "http://www.test.org/myOntologyTemplate#template-output-entity-1"
b.createAgentBehaviorTemplate("MyAgentBehaviorTemplate", "MyTemplateBehavior", "MyTemplateGoal", "MyTemplateTask",
                         ["MyTemplateTaskOperator", "turn"],
                         ["MyTemplateOperatorArgument", "off"],
                         [
                             ["MyTemplateTaskObject","refersAsNewTo", object1 ]
                         ],
                         [
                             ["MyTemplateInput1", "refersAsNewTo", input1]
                         ],
                         [
                             ["MyTemplateOutput1", "refersAsNewTo", output1]
                         ])
#connect agent to agent behavior
#b.connectAgentTemplateToBehavior("MyAgentBehaviorTemplate", "MyTemplateBehavior")

#Create agent
b.createAgent("MyAgent")
#create agent behavior
agentobject1 = "http://www.test.org/myOntology#agent-object-entity-1"
agentinput1 = "http://www.test.org/myOntology#agent-input-entity-1"
agentoutput1 = "http://www.test.org/myOntology#agent-output-entity-1"
b.createAgentBehavior("MyAgent", "MyAgentBehavior", "MyAgentGoal", "MyAgentTask",
                         ["MyAgentTaskOperator", "turn"],
                         ["MyAgentOperatorArgument", "off"],
                         [
                             ["MyAgentTaskObject", "refersAsNewTo", agentobject1]
                         ],
                         [
                             ["MyAgentInput1", "refersAsNewTo", agentinput1]
                         ],
                         [
                             ["MyAgentOutput1", "refersAsNewTo", agentoutput1]
                         ],
                         [
                          "MyTemplateTask",
                          [
                              ["MyAgentTaskObject", "MyTemplateTaskObject"]
                          ],
                          [
                              ["MyAgentInput1", "MyTemplateInput1"]
                          ],
                          [
                              ["MyAgentOutput1", "MyTemplateOutput1"]
                          ]
                         ])
#connect agent to agent behavior
#b.connectAgentToBehavior("MyAgent", "MyAgentBehavior")


executionobject1 = "http://www.test.org/myExecOntology#execution-object-entity-1"
executioninput1 = "http://www.test.org/myExecOntology#execution-input-entity-1"
executionoutput1 = "http://www.test.org/myExecOntology#execution-output-entity-1"
#creating agent action
b.createAgentAction("MyAgent", "planExecution", "executionGoal", "executionTask",
                         ["executionOperator", "turn"],
                         ["executionArgument", "off"],
                         [
                             ["executionObject", "refersExactlyTo", executionobject1]
                         ],
                         [
                             ["executionInput1", "refersExactlyTo", executioninput1]
                         ],
                         [
                             ["executionOutput1", "refersExactlyTo", executionoutput1]
                         ],
                         [
                          "MyAgentTask",
                          [
                              ["executionObject", "MyAgentTaskObject"]
                          ],
                          [
                              ["executionInput1", "MyAgentInput1"]
                          ],
                          [
                              ["executionOutput1", "MyAgentOutput1"]
                          ]
                         ])


#creating Plan
planobject1 = "http://www.test.org/myPlanOntology#plan-object-entity-1"
planinput1 = "http://www.test.org/myPlanOntology#plan-input-entity-1"
planoutput1 = "http://www.test.org/myPlanOntology#plan-output-entity-1"
#creating agent plan
b.createAgentPlanRequestDescription("MyAgent", "planDescription", "planGoal", "planTask",
                         ["planOperator", "turn"],
                         ["planArgument", "off"],
                         [
                             ["planObject", "refersAsNewTo", planobject1]
                         ],
                         [
                             ["planInput1", "refersAsNewTo", planinput1]
                         ],
                         [
                             ["planOutput1", "refersAsNewTo", planoutput1]
                         ])






#serialization
print("######################Agent################################")
print(ontology.serialize(format="turtle"))
print("######################Template################################")
print(ontologyTemp.serialize(format="turtle"))
print("#####################Action#################################")
print(ontologyAct.serialize(format="turtle"))
print("#####################Plan#################################")
print(ontologyPlan.serialize(format="turtle"))
#saving
file = open("ontologies/agent.owl", "w")
file.write(ontology.serialize(format='xml'))

file = open("ontologies/agentTemplate.owl", "w")
file.write(ontologyTemp.serialize(format='xml'))

file = open("ontologies/agentAction.owl", "w")
file.write(ontologyAct.serialize(format='xml'))

file = open("ontologies/agentPlan.owl", "w")
file.write(ontologyPlan.serialize(format='xml'))