# OASIS - An ontology for Agent, Systems, and Integration of Services


# Projects based on OASIS

- CLARA (former PROFONTO) https://github.com/dfsantamaria/CLARA
- POC4COMMERCE NGI-ONTOCHAIN https://github.com/dfsantamaria/POC4COMMERCE

# Papers and articles

-  The Ontology for Agents, Systems and Integration of Services: recent advancements of OASIS. Giampaolo Bella, Domenico Cantone, Marianna Nicolosi-Asmundo, Daniele Francesco Santamaria. Proceedings of WOA 2022- 23nd Workshop From Objects to Agents, 1–2, September 2022, Genova, Italy, CEUR Workshop Proceedings, ISSN 1613-0073, Vol. 3261, pp.176--193.
-  Blockchains through ontologies: the case study of the Ethereum ERC721 standard in OASIS. Giampaolo Bella, Domenico Cantone, Cristiano Longo, Marianna Nicolosi-Asmundo, Daniele Francesco Santamaria. In D. Camacho et al. (eds.), Intelligent Distributed Computing XIV, Studies in Computational Intelligence 1026, Chapter 23,  pp. 249-259.
-  Semantic Representation as a Key Enabler for Blockchain-Based Commerce. Giampaolo Bella, Domenico Cantone, Cristiano Longo, Marianna Nicolosi-Asmundo and Daniele Francesco Santamaria. In: K. Tserpes et al. (Eds.): GECON 2021, Lecture Note in Computer Science, Vol. 13072, pp. 191–198, Springer, 2021.
-  Ontological Smart Contracts in OASIS: Ontology forAgents, Systems, and Integration of Services. Domenico Cantone, Carmelo Fabio Longo, Marianna Nicolosi-Asmundo, Daniele Francesco Santamaria, Corrado Santoro. In D. Camacho et al. (eds.), Intelligent Distributed Computing XIV, Studies in Computational Intelligence 1026, Chapter 22, pp. 237-247.
-  Towards an Ontology-Based Framework for a Behavior-Oriented Integration of the IoT. Domenico Cantone, Carmelo Fabio Longo, Marianna Nicolosi-Asmundo, Daniele Francesco Santamaria, Corrado Santoro. Proceedings of the 20th Workshop From Objects to Agents, 26-28 June, 2019, Parma, Italy, CEUR Workshop Proceedings, ISSN 1613-0073, Vol. 2404, pp. 119--126.
- Giampaolo Bella, Gianpietro Castiglione, Daniele Francesco Santamaria. A Behaviouristic Approach to Representing Processes and Procedures in the OASIS 2 Ontology (2023) CEUR Workshop Proceedings 3637.
-  Giampaolo Bella, Domenico Cantone, Carmelo Fabio Longo, Marianna Nicolosi Asmundo, Daniele Francesco Santamaria. The ontology for agents, systems and integration of services: OASIS version 2.
Intelligenza Artificiale 2023, 17(1), pp. 51–62.
-  Giampaolo Bella, Domenico Cantone, Gianpietro Castiglione, Marianna Nicolosi Asmundo, Daniele Francesco Santamaria. A behaviouristic semantic approach to blockchain-based e-commerce. Semantic Web
(2024), 15 (5), pp. 1863 - 1914. DOI: 10.3233/SW-243543.
-  Giamapolo Bella, Domenico Cantone, Marianna Nicolosi Asmundo, Daniele Francesco Santamaria. Towards a semantic blockchain: A behaviouristic approach to modelling Ethereum. (2024) Applied Ontology, 19 (2), pp. 143 - 180, DOI: 10.3233/AO-230010.

## Licensing information
Copyright (C) 2021.  Giampaolo Bella, Domenico Cantone, Marianna Nicolosi Asmundo, Daniele Francesco Santamaria. This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version. This program is distributed in the hope that it will be useful,  but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.  You should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Python BehaviorManager module
This program permits the creation of OASIS agents.

## Requirements </br>
   - Python interpreter version 3.7 or greater.
   - RDFLib version 6.1.1.

## Generating new agents and agent behaviors </br>

In order to generate new OASIS behaviors you should

A)  Create three RDFLib ontology objects, one for the ontology hosting the agent behaviors, one for the ontology hosting the agent templates, one for the ontology hosting data.

Create a BehaviorManager object by typing: </br>
      
      b = BehaviorManager(ontology, namespace, ontologyURL, ontologyTemplate, namespaceTemplate, templateURL)
      
   where:  </br>
   - "ontology" is the ontology containing the agent behavior.
   - "namespace" is namespace of "ontology". You can use "None" if "xml:base" is already defined in the ontology.
   - "ontologyURL" is the URL of the ontology.
   - "ontologyTemplate" is the namespace of the ontology containing the behavior template.
   - "namespaceTemplate" is namespace of "ontologyTemplate". You can use "None" if "xml:base" is already defined in the ontology.
   - "templateURL" is the URL of the ontology containing the behavior template.
   
B) (Optional) Create a new behavior template by typing </br>
      
      b.createAgentTemplate(agentTemplateName)
      
   where:  </br>   
   - "ontologyTemplateName" is the name of the agent template name. </br>
   
   Then, create a new agent template behavior by typing: </br>


      b.createAgentBehaviorTemplate(MyTemplateBehavior, MyTemplateGoal, MyTemplateTask,
                                     [MyTemplateTaskOperator, action], 
                                     [MyTemplateOperatorArgument, actionArgument],
                                     [
                                        [MyTemplateTaskObject, taskObjectProperty, objectTemplate]
                                     ], 
                                     [ 
                                        [MyTemplateInput1, taskInputProperty, input1]
                                     ], 
                                     [ 
                                        ["MyTemplateOutput1", taskOutputProperty, output1]
                                     ])

        
   where:
   - "MyTemplateBehavior" is the entity name of the behavior template. 
   - "MyTemplateGoal" is the entity name of the goal template.
   - "MyTemplateTask" is the entity name of the task template.
   - "MyTemplateTaskOperator" and "action" are, respectively, the entity name of the task operator  and the operator action as defined in OASIS-ABox.
   - "MyTemplateOperatorArgument" and "actionArgument" are, respectively, the entity name of the operator argument and the operator argument as defined in OASIS-ABox.
   - A list of elements of the form:
     - [MyTemplateTaskObject, taskObjectProperty, objectTemplate] </br>
       where: </br>
         - "MyTemplateTaskObject" is the entity name of the task object.
         - "taskObjectProperty" is the either "refersAsNewTo" or "refersExactlyTo".
         - "objectTemplate" is the element associated to the task object.
   - A list of elements of the form:
     - [MyTemplateInput1, taskInputProperty, input1] </br>
       where: </br> 
        - "MyTemplateInput1" is the entity name of the input.
        - "taskInputProperty" is the either "refersAsNewTo" or "refersExactlyTo".
        - "input" is the element associated to the input element.   
   - A list of elements of the form:
     - [MyTemplateOutput1, taskOutputProperty, output1] </br>
       where: </br> 
       - "MyTemplateOutput1" is the entity name of the output.
       - "taskOutputProperty" is either "refersAsNewTo" or "refersExactlyTo".
       - "output" is the element associated with the output element.  
     
 - Connect the behavior with the related template
 
       b.connectAgentTemplateToBehavior(MyAgentBehaviorTemplate, MyTemplateBehavior)
       
   where: </br>
   - "MyAgentBehaviorTemplate" is the the behavior template created as described above.
   - "MyTemplateBehavior" is the behavior created as above.

C) Create a new agent and a new behavior eventually related with a behavior template.
   
   Create a new agent by typing:
              
      b.createAgent("MyAgent")
  
   where:
   - "MyAgent" is the entity name of the agent.
   
   Create a new agent behavior and eventually connect it to its template by typing
   
      b.createAgentBehavior(MyAgentBehavior, MyAgentGoal, MyAgentTask,
                            [MyAgentTaskOperator, action],
                            [MyAgentOperatorArgument, actionArgument],
                         [
                            [MyAgentTaskObject, taskObjectProperty, agentobject1]
                         ],
                         [
                             [MyAgentInput1, taskInputProperty, agentinput1]
                         ],
                         [
                             [MyAgentOutput1, taskInputProperty, agentoutput1]
                         ],
                         [
                           MyTemplateTask,
                          [
                              [MyAgentTaskObject, MyTemplateTaskObject]
                          ],
                          [
                              [MyAgentInput1, MyTemplateInput1]
                          ],
                          [
                              [MyAgentOutput1, MyTemplateOutput1]
                          ]
                         ])

   where:
   - "MyAgentBehavior" is the entity name of the behavior. 
   - "MyAgentGoal" is the entity name of the goal.
   - "MyAgentTask" is the entity name of the task.
   - "MyAgentTaskOperator" and "action" are, respectively, the entity name of the task operator  and the operator action as defined in OASIS-ABox.
   - "MyAgentOperatorArgument" and "actionArgument" are, respectively, the entity name of the operator argument and the operator argument as defined in OASIS-ABox.
   - A list of elements of the form:
        - [MyAgentTaskObject, taskObjectProperty, agentobject1] </br>
           where: </br>
           - "MyAgentTaskObject" is the entity name of the task object.
           - "taskObjectProperty" is the either "refersAsNewTo" or "refersExactlyTo".
           - "agentobject1" is the element associated to the task object.
   - A list of elements of the form:
        - [MyAgentInput1, taskInputProperty, agentinput1] </br>
          where: </br> 
          - "MyAgentInput1" is the entity name of the input.
          - "taskInputProperty" is the either "refersAsNewTo" or "refersExactlyTo".
          - "agentinput1" is the element associated to the input element.   
   - A list of elements of the form:
        - [MyAgentOutput1, taskOutputProperty, agentoutput1]</br>
          where: </br> 
          - "MyAgentOutput1" is the entity name of the output.
          - "taskOutputProperty" is the either "refersAsNewTo" or "refersExactlyTo".
          - "agentoutput1" is the element associated to the output element. 
   - Eventually a list of elements mapping from the agent to the template:
       - "MyTemplateTask" is the task object of the behavior template.
       - A list of elements of the form:
            - ["MyAgentTaskObject", "MyTemplateTaskObject"] </br>
              where:</br>
                 -  "MyAgentTaskObject", "MyTemplateTaskObject" represent the entity name of the agent task object  and the entity of the task object template, respectively.
       - A list of elements of the form:  
            - ["MyAgentInput1", "MyTemplateInput1"] </br>
              where:</br>
                -  "MyAgentInput1", "MyTemplateInput1" represent the entity name of the agent input and the agent input template, respectively.
       - A list of elements of the form:  
           - ["MyAgentOutput1", "MyTemplateOutput1"] </br>
           where:</br>
               -  "MyAgentOutput1", "MyTemplateOutput1" represent the entity name of the agent output and the agent output template, respectively.
  - Connect the created behavior to its agent by typing:
     
        b.connectAgentToBehavior("MyAgent", "MyAgentBehavior")
    
    where: </br>
    - "MyAgent" and "MyAgentBehavior" are, respectively, the agent and the agent behavior.
    
       
 D) Generate a new action and connect it to the related behavior by typing
 
       b.createAgentAction(MyAgent, planExecution, executionGoal, executionTask,
                         [executionOperator, action],
                         [executionArgument, argument],
                         [
                             [executionObject, taskObjectProperty, executionobject1]
                         ],
                         [
                             [executionInput1, inputProp, executioninput1]
                         ],
                         [
                             [executionOutput1, outputProp, executionOutput1]
                         ],
                         [
                           MyAgentTask,
                          [
                              [executionObject, MyAgentTaskObject]
                          ],
                          [
                              [executionInput1, MyAgentInput1]
                          ],
                          [
                              [executionOutput1, MyAgentOutput1]
                          ]
                         ])
                         
  where:</br>
  - "MyAgent" is the entity name of the agent responsible for the execution of the action.
  - "planExecution" is the entity name of the plan execution.
  - "executionGoal" is the entity name of the goal execution.
  - "executionTask" is the entity name of the task execution.
  - A list of element of the form:
      - [executionOperator, action] </br>
        where:</br>
         - "executionOperator" is the name of the task operator.
         - "action" is name of the action as defined in OASIS-ABox.
      - [executionArgument, argument] </br>
        where:</br>
        - "executionArgument" is the name of the task argument.
        - "argument" is the name of the argument as defined in OASIS-ABox.
      - A list of element of the form:  
        - [executionObject, taskObjectProperty, executionobject1] </br>
          where: </br>
          - "executionObject" is the entity name of the task execution object.
          - "taskObjectProperty" is  either "refersAsNewTo" or "refersExactlyTo".
          - "executionobject1" is the element associated with the task execution object.     
      - A list of elements of the form:
        - [executionInput1, inputProp, executioninput1] </br>
          where: </br>
             - "executionInput1" is the entity name of task input.
             - "inputProp" is either "refersAsNewTo" or "refersExactlyTo".
             - "executioninput1" is the element associated with the task input.
       - A list of elements of the form:
         - [executionOutput1, outputProp, executionOutput1] </br>
           where: </br>
             - "executionOutput1" is the entity name of task output.
             - "outputProp" is either "refersAsNewTo" or "refersExactlyTo".
             - "executionOutput1" is the element associated with the task output.
       - A list of elements mapping from the agent action to the agent behavior:
          - "MyAgentTask" is the task  of the agent behavior.
       - A list of elements of the form:
          - [executionObject, MyAgentTaskObject] </br>
            where: </br>
              - "executionObject", "MyAgentTaskObject" represent the entity name of the  task execution  and the entity name of the task object of the agent behavior, respectively.
       - A list of elements of the form:  
         - [executionInput1, MyAgentInput1] </br>
           where:</br>
              - "executionInput1", "MyAgentInput1" represent the entity name of the action input and the agent behavior input , respectively.
        - A list of elements of the form:  
          - [executionOutput1, MyAgentOutput1] </br>
            where:</br>
              -  "executionOutput1", "MyAgentOutput1" represent the entity name of the action output and the agent behavior output, respectively.



Check the file
- OASIS-MAN\Python\test\Test-BehaviorManager.py

for an example.
