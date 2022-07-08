from rdflib import *

class BehaviorManager:
    def __init__(self, ontologyGraph, ontologyNamespace, ontologyURL,
                       ontologyTemplateGraph, ontologyTemplateNamespace, templateURL,
                       actionGraph, actionNamespace, actionURL,
                       planGraph, planNamespace, planURL): # INPUT: the user ontology, the user ontology namespace
        #map name:[URL, namespace, number]
        self.ontoMap = {}
        self.ontologies = [None, None, None, None, None, None]
        #
        #oasis ontology data
        #
        self.addOntoMap("oasis", "https://www.dmi.unict.it/santamaria/projects/oasis/sources/oasis.owl", None, 0)  # OASIS ontology object
        self.ontologies[self.ontoMap["oasis"]["onto"]]=self.loadOntology(self.ontoMap["oasis"]["url"])
        self.addOntoMap("abox", "https://www.dmi.unict.it/santamaria/projects/oasis/sources/oasis-abox.owl",None, 1)  # OASIS-ABox ontology object
        self.ontologies[self.ontoMap["abox"]["onto"]] = self.loadOntology(self.ontoMap["abox"]["url"])

        self.owlobj = URIRef("http://www.w3.org/2002/07/owl#ObjectProperty")
        self.owldat = URIRef("http://www.w3.org/2002/07/owl#DatatypeProperty")
        self.addOntoMap("oasis", None, self.getNamespace(self.ontologies[self.ontoMap["oasis"]["onto"]]), None)# OASIS ontology namespace
        self.addOntoMap("abox", None, self.getNamespace(self.ontologies[self.ontoMap["abox"]["onto"]]), None)  # OASIS-ABox ontology namespace

        if ontologyTemplateGraph is not None:
            self.startOntology("template", templateURL, ontologyTemplateNamespace, ontologyTemplateGraph, 2, None)

        self.startOntology("base", ontologyURL, ontologyNamespace, ontologyGraph, 3, {"template"})
        if actionGraph is not None:
            self.startOntology("action", actionURL, actionNamespace, actionGraph, 4, {"base"})

        if planGraph is not None:
            self.startOntology("plan", planURL, planNamespace, planGraph, 5, {"action","base"})

        return


    def startOntology(self, shortName, url, namespace, graph, pos, toimport):
        if pos==None:
           nwpos=len(self.ontoMap)
           self.ontologies.append(None)
        else:
           nwpos=pos
        self.addOntoMap(shortName, url, None, nwpos)
        self.ontologies[self.ontoMap[shortName]["onto"]] = graph  # User template ontology
        if len([item for item in self.ontologies[self.ontoMap[shortName]["onto"]].namespaces() if item[1] == 'http://www.w3.org/2002/07/owl#'])==0:
            self.ontologies[self.ontoMap[shortName]["onto"]].bind("owl","http://www.w3.org/2002/07/owl#")
        if len([item for item in self.ontologies[self.ontoMap[shortName]["onto"]].namespaces()
                if item[1] == self.ontoMap["oasis"]["namespace"]]) == 0:
                self.ontologies[self.ontoMap[shortName]["onto"]].bind("oasis", self.ontoMap["oasis"]["namespace"])
        if len([item for item in self.ontologies[self.ontoMap[shortName]["onto"]].namespaces()
                if item[1] == self.ontoMap["abox"]["namespace"]]) == 0:
                 self.ontologies[self.ontoMap[shortName]["onto"]].bind("oabox", self.ontoMap["abox"]["namespace"])

        if namespace is None:
            self.addOntoMap(shortName, None, self.getNamespace(self.ontologies[self.ontoMap[shortName]["onto"]]), None)
        else:
            self.addOntoMap(shortName, None, namespace, None)
        if toimport is not None and len(toimport)>0:
            for im in toimport:
               if self.ontoMap[shortName]["namespace"] != self.ontoMap[im]["namespace"]:
                   self.addImportAxioms(self.ontologies[self.ontoMap[shortName]["onto"]], self.ontoMap[shortName]["namespace"],
                                 [self.ontoMap[im]["namespace"]])

        return

    def getValue(self):
        return self.value

    #add an entry to the ontology map
    def addOntoMap(self, name, url, namespace, onto):
        if name not in self.ontoMap:
           if onto is None:
              position = len(self.ontoMap)
           else:
              position = onto
           self.ontoMap[name]={"url": None,"namespace": None,"onto": position}
        if url is not None:
           self.ontoMap[name]["url"]=url
        if namespace is not None:
           self.ontoMap[name]["namespace"]=namespace
        if onto is not None:
           self.ontoMap[name]["onto"]= onto

    #create an ontology object from a given URL
    def loadOntology(self, ontoURL):
        g=Graph()
        g.load(ontoURL)
        return g

    # Get the base namespace of an ontology given the ontology object
    def getNamespace(self, ontology):
        namespace = ""
        for ns_prefix, ns_namespace in ontology.namespaces():
            if ns_prefix == "":
               namespace=ns_namespace
        if not namespace.endswith('#'):
            return namespace+"#"
        return namespace

    # Get the IRI of OASIS entities given their entity name
    def getOASISEntityByName(self, name):
        return self.ontoMap["oasis"]["namespace"] + name

    # Get the IRI of OASIS-Abox entities given their entity name
    def getOASISABoxEntityByName(self, name):
        return self.ontoMap["abox"]["namespace"] + name

    def addObjPropAssertion(self, ontology, subject, property, object):
        self.addOWLObjectProperty(ontology, property)
        ontology.add((URIRef(subject), URIRef(property), URIRef(object)))

    def addDataPropAssertion(self, ontology, subject, property, object, dtype):
        self.addOWLDataProperty(ontology, property)
        ontology.add((URIRef(subject), URIRef(property), Literal(object, datatype=dtype)))

    def addClassAssertion(self, ontology, instance, owlclass):
        ontology.add((URIRef(instance), RDF.type, URIRef(owlclass)))

    def addOWLObjectProperty(self, ontology, property):
        self.addClassAssertion(ontology, property, self.owlobj)

    def addOWLDataProperty(self, ontology, property):
        self.addClassAssertion(ontology, property, self.owldat)

    # Add to ontology with the selected namespace an owl:imports axiom for each passed IRI.
    #INPUT the ontology and the ontology IRI that will include the owl:imports axiom, a list of IRI to be included in the ontology
    def addImportAxioms(self, ontology, ontologyNS, namespaceToImport):
        for s in namespaceToImport:
            self.addObjPropAssertion(ontology, URIRef(ontologyNS), OWL.imports, URIRef(s))


    def getNoAnchorNamespace(self, namespace):
        if namespace.endswith('#'):
           return namespace[:-1]
        return namespace

    #import OASIS and OASIS-Abox in the current ontology
    def addImportOASIS(self, ontology, namespace):
        self.addImportAxioms(ontology, namespace, [self.ontoMap["oasis"]["url"], self.ontoMap["abox"]["url"]])
        ontology.bind("oasis", self.ontoMap["oasis"]["namespace"])
        ontology.bind("oabox", self.ontoMap["abox"]["namespace"])

        # Create an user agent given the agent entity name

    def createAgent(self, agentName):
        self.baseAgent = self.ontoMap["base"]["namespace"] + agentName
        self.addClassAssertion(self.ontologies[self.ontoMap["base"]["onto"]], self.baseAgent, self.getOASISEntityByName("Agent"))
        return self.baseAgent


    #create an OASIS agent template given its name
    def createAgentTemplate(self, agentName):
        baseTemplateAgent = self.ontoMap["template"]["namespace"] + agentName
        self.addClassAssertion(self.ontologies[self.ontoMap["template"]["onto"]], baseTemplateAgent, self.getOASISEntityByName("AgentBehaviorTemplate"))
        # print(self.baseNamespace, self.oasisNamespace, self.oasisABoxNamespace)
        return baseTemplateAgent


    #connect a agent template  with a behavior
    def connectAgentTemplateToBehavior(self, agentName, behaviorName):
        self.__connectAgentToGeneralBehavior__(self.ontologies[self.ontoMap["template"]["onto"]], self.ontoMap["template"]["namespace"], agentName, behaviorName)

    # connect a agent  with a behavior
    def connectAgentToBehavior(self, agentName, behaviorName):
        self.__connectAgentToGeneralBehavior__(self.ontologies[self.ontoMap["base"]["onto"]], self.ontoMap["base"]["namespace"], agentName, behaviorName)

    def __connectAgentToGeneralBehavior__(self, ontology, namespace, agentName, behaviorName):
        self.addObjPropAssertion(ontology, namespace + agentName,  self.getOASISEntityByName("hasBehavior"), namespace + behaviorName)


    #add a goal to a selected behavior given the behavior IRI and goal name
    def addGoalToBehavior(self, ontology, namespace, behavior, goalName):
        goal = namespace + goalName
        self.addClassAssertion(ontology, goal, self.getOASISEntityByName("GoalDescription"))
        self.addObjPropAssertion(ontology, behavior, self.getOASISEntityByName("consistsOfGoalDescription"), goal)
        return goal

    # add a goal to a selected behavior given the behavior IRI and goal name
    def addGoalExecutionToPlan(self, ontology, namespace, plan, goalName):
        goal = namespace + goalName
        self.addClassAssertion(ontology, goal, self.getOASISEntityByName("GoalExecution"))
        self.addObjPropAssertion(ontology, plan, self.getOASISEntityByName("consistsOfGoalExecution"), goal)
        return goal

    #add a task to a selected goal given the goal IRI and the task name
    def addTaskToGoal(self, ontology, namespace, goal, taskName):
        task = namespace + taskName
        self.addClassAssertion(ontology, task, self.getOASISEntityByName("TaskDescription"))
        self.addObjPropAssertion(ontology, goal, self.getOASISEntityByName("consistsOfTaskDescription"), task)
        return task

    # add a task to a selected goal given the goal IRI and the task name
    def addTaskExecutionToGoal(self, ontology, namespace, goal, taskName):
        task = namespace + taskName
        self.addClassAssertion(ontology, task, self.getOASISEntityByName("TaskExecution"))
        self.addObjPropAssertion(ontology, goal, self.getOASISEntityByName("consistsOfTaskExecution"), task)
        return task

    #add a task operator to the selected task given the task IRI, the operator name and the operator entity name
    def addTaskOperatorToTask(self, ontology, namespace, task, operatorName, operatorEntity):
        taskOperator = namespace + operatorName
        self.addClassAssertion(ontology, taskOperator, self.getOASISEntityByName("TaskOperator"))
        self.addObjPropAssertion(ontology, task, self.getOASISEntityByName("hasTaskOperator"), taskOperator)
        self.addObjPropAssertion(ontology, taskOperator, self.getOASISEntityByName("refersExactlyTo"),
                                 self.getOASISABoxEntityByName(operatorEntity))  # the action
        self.addClassAssertion(ontology, self.getOASISABoxEntityByName(operatorEntity), self.getOASISEntityByName("Action"))
        return taskOperator

    #add a task operator argument to selected task given the task IRI, the operator argument name and the operator argument entity name
    def addTaskOperatorArgumentToTask(self, ontology, namespace, task, taskOpArgumentName, taskOpEntityName):
        taskOperatorArgument = namespace + taskOpArgumentName
        self.addClassAssertion(ontology, taskOperatorArgument, self.getOASISEntityByName("TaskOperatorArgument"))
        self.addObjPropAssertion(ontology, task, self.getOASISEntityByName("hasTaskOperatorArgument"),
                                 taskOperatorArgument)
        self.addObjPropAssertion(ontology, taskOperatorArgument, self.getOASISEntityByName("refersExactlyTo"),
                                 self.getOASISABoxEntityByName(taskOpEntityName))  # the action
        self.addClassAssertion(ontology, self.getOASISABoxEntityByName(taskOpEntityName), self.getOASISEntityByName("DescriptionObject"))
        return taskOperatorArgument

    def __createBehaviorPath__(self, ontology, namespace, behaviorName, goalName, taskName, operators,  operatorsArguments):
        return self.__createPlanPath__(ontology, namespace, behaviorName, "Behavior", goalName, taskName, operators, operatorsArguments)

    def __createPlanPath__(self, ontology, namespace, planName, className, goalName, taskName, operators, operatorsArguments):
        behavior = namespace + planName
        self.addClassAssertion(ontology, behavior, self.getOASISEntityByName(className))

        # create, add, and connect the goal
        goal = self.addGoalToBehavior(ontology, namespace, behavior, goalName)

        # create, add, and connect the task
        task = self.addTaskToGoal(ontology, namespace, goal, taskName)

        # create, add, and connect the task operator
        taskOperator = self.addTaskOperatorToTask(ontology, namespace, task, operators[0], operators[1]);

        # create, add, and connect the task operator argument
        if operatorsArguments:
            taskOperatorArgument = self.addTaskOperatorArgumentToTask(ontology, namespace, task, operatorsArguments[0], operatorsArguments[1])
        else:
            taskOperatorArgument = None
        return behavior, goal, task, taskOperator, taskOperatorArgument

    def __createExecutionPath__(self, ontology, namespace, planName, PlanClass, goalName, taskName, operators, operatorsArguments):
        plan = namespace + planName
        self.addClassAssertion(ontology, plan, self.getOASISEntityByName(PlanClass))

        # create, add, and connect the goal
        goal = self.addGoalExecutionToPlan(ontology, namespace, plan, goalName)

        # create, add, and connect the task
        task = self.addTaskExecutionToGoal(ontology, namespace, goal, taskName)

        # create, add, and connect the task operator
        taskOperator = self.addTaskOperatorToTask(ontology, namespace, task, operators[0], operators[1]);

        # create, add, and connect the task operator argument
        if operatorsArguments:
            taskOperatorArgument = self.addTaskOperatorArgumentToTask(ontology, namespace, task, operatorsArguments[0], operatorsArguments[1])
        else:
            taskOperatorArgument = None
        return plan, goal, task, taskOperator, taskOperatorArgument


    # add task object to the selected task given the object name,  the task obj entity property, and the task object entity
    def addTaskObjectToTask(self, ontology, namespace, task, objectName, taskobpropentity, taskobentity):
        return self.__addTaskElementToTask__(ontology, namespace, task, objectName,  "TaskObject", "hasTaskObject", taskobpropentity, taskobentity)

    # add task object template to the selected task given the object name,  the task obj entity property, and the task object entity
    def addTaskObjectTemplateToTask(self, task, objectName,  taskobpropentity, taskobentity):
        return  self.__addTaskElementToTask__(self.ontologies[self.ontoMap["template"]["onto"]], self.ontoMap["template"]["namespace"], task, objectName, "TaskObjectTemplate", "hasTaskObjectTemplate", taskobpropentity, taskobentity)

    def addTaskFormalInputToBehaviorTask(self, task, input, inputPropEntity, inputEntity):
        return self.__addTaskFormalInputToTask__(self.ontologies[self.ontoMap["base"]["onto"]], self.ontoMap["base"]["namespace"], task, input, inputPropEntity, inputEntity)

    def addTaskFormalInputToPlanTask(self, task, input, inputPropEntity, inputEntity):
        return self.__addTaskFormalInputToTask__(self.ontologies[self.ontoMap["plan"]["onto"]], self.ontoMap["plan"]["namespace"], task, input, inputPropEntity, inputEntity)

    # add task input to the selected task given the input name, the input entity property,  and the input entity
    def __addTaskFormalInputToTask__(self, ontology, namespace, task, input, inputPropEntity, inputEntity):
        return self.__addTaskElementToTask__(ontology,namespace, task, input, "TaskFormalInputParameter", "hasTaskFormalInputParameter", inputPropEntity, inputEntity)

    # add task input to the selected task given the input name, the input entity property,  and the input entity
    def addTaskActualInputToTask(self, ontology, namespace, task, input, inputPropEntity, inputEntity):
            return self.__addTaskElementToTask__(ontology, namespace, task, input,
                                                 "TaskActualInputParameter", "hasTaskActualInputParameter",
                                                 inputPropEntity, inputEntity)

    # add task input to the selected task given the input name, the input entity property,  and the input entity
    def addTaskInputTemplateToTask(self, task, input, inputPropEntity, inputEntity):
        return self.__addTaskElementToTask__(self.ontologies[self.ontoMap["template"]["onto"]], self.ontoMap["template"]["namespace"], task, input, "TaskInputParameterTemplate", "hasTaskInputParameterTemplate", inputPropEntity, inputEntity)


    def addTaskFormalOutputToPlanTask(self, task, output, outputPropEntity, outputEntity):
        return self.__addTaskFormalOutputToTask__(self.ontologies[self.ontoMap["plan"]["onto"]],
                                              self.ontoMap["plan"]["namespace"], task, output, outputPropEntity,
                                              outputEntity)

    def addTaskFormalOutputToBehaviorTask(self,  task, output, outputPropEntity, outputEntity):
        return self.__addTaskFormalOutputToTask__(self.ontologies[self.ontoMap["base"]["onto"]], self.ontoMap["base"]["namespace"], task, output, outputPropEntity, outputEntity)

    # add task output to the selected task given the output name, the output entity property,  and the output entity
    def __addTaskFormalOutputToTask__(self, ontology, namespace, task, output, outputPropEntity, outputEntity):
        return self.__addTaskElementToTask__(ontology, namespace, task, output,  "TaskFormalOutputParameter", "hasTaskFormalOutputParameter", outputPropEntity,
                                             outputEntity)

    def addTaskActualOutputToTask(self, ontology, namespace, task, output, outputPropEntity, outputEntity):
        return self.__addTaskElementToTask__(ontology, namespace, task, output,
                                             "TaskActualOutputParameter", "hasTaskActualOutputParameter",
                                             outputPropEntity,
                                             outputEntity)

    # add task input to the selected task given the input name, the input entity property,  and the input entity
    def addTaskOutputTemplateToTask(self, task, output, outputPropEntity, outputEntity):
        return self.__addTaskElementToTask__(self.ontologies[self.ontoMap["template"]["onto"]], self.ontoMap["template"]["namespace"], task, output,  "TaskOutputParameterTemplate", "hasTaskOutputParameterTemplate",
                                             outputPropEntity, outputEntity)

    # add task element to the selected task given the  name, the  class, the elementt property, the element entity property,  and the element entity
    def __addTaskElementToTask__(self, ontology, namespace, task, elementName, elementclass, elemobprop, elempropentity, elementity):
        object = namespace + elementName
        self.addClassAssertion(ontology, object, self.getOASISEntityByName(elementclass))
        self.addObjPropAssertion(ontology, task, self.getOASISEntityByName(elemobprop), object)
        self.addObjPropAssertion(ontology, object, self.getOASISEntityByName(elempropentity),
                                 elementity)  # the object
        return object

    #create a behavior template given an agent template IRI
    def createAgentBehaviorTemplate(self, behaviorName, goalName, taskName, operators, operatorsArguments, objects, inputs, outputs):
        #create  and add the behavior
        behavior, goal, task, taskOperator, taskOperatorArgument = self.__createBehaviorPath__(self.ontologies[self.ontoMap["template"]["onto"]], self.ontoMap["template"]["namespace"], behaviorName, goalName, taskName, operators, operatorsArguments)
        #create, add, and connect the task object
        if objects:
           for object in objects:
               objectName = self.addTaskObjectTemplateToTask(task, object[0], object[1], object[2])

        # create, add, and connect the task input parameters
        if inputs:
            for input in inputs:
                inputName = self.addTaskInputTemplateToTask(task, input[0], input[1], input[2])

        # create, add, and connect the task input parameters
        if outputs:
           for output in outputs:
               outputName = self.addTaskOutputTemplateToTask(task, output[0], output[1], output[2])

    def createAgentBehavior(self, behaviorName, goalName, taskName, operators, operatorsArguments, objects, inputs,  outputs, mapping):
        # create  and add the behavior
        behavior, goal, task, taskOperator, taskOperatorArgument  = self.__createBehaviorPath__(self.ontologies[self.ontoMap["base"]["onto"]],  self.ontoMap["base"]["namespace"], behaviorName, goalName, taskName, operators, operatorsArguments)
        # create, add, and connect the task object
        if objects:
            for object in objects:
                objectName = self.addTaskObjectToTask(self.ontologies[self.ontoMap["base"]["onto"]], self.ontoMap["base"]["namespace"], task, object[0], object[1], object[2])


        # create, add, and connect the task input parameters
        if inputs:
           for input in inputs:
               inputName = self.addTaskFormalInputToBehaviorTask(task, input[0], input[1], input[2])


        # create, add, and connect the task input parameters
        if outputs:
           for output in outputs:
               outputName = self.addTaskFormalOutputToBehaviorTask(task, output[0], output[1], output[2])

        #linking agent behavior with the corresponding behavior template
        if mapping:
            #mapping the task
            task_op= URIRef(self.ontoMap["template"]["namespace"]+mapping[0])
            self.addObjPropAssertion(self.ontologies[self.ontoMap["base"]["onto"]], task, self.getOASISEntityByName("overloads"), task_op)  # the action

            # mapping the task operator (automatically)
            for object in self.ontologies[self.ontoMap["template"]["onto"]].objects(task_op, self.getOASISEntityByName("hasTaskOperator")):
                self.addObjPropAssertion(self.ontologies[self.ontoMap["base"]["onto"]], taskOperator, self.getOASISEntityByName("overloads"), object)
                break
            # mapping the task operator argument (automatically) #
            for object in self.ontologies[self.ontoMap["template"]["onto"]].objects(task_op, self.getOASISEntityByName("hasTaskOperatorArgument")):
                self.addObjPropAssertion(self.ontologies[self.ontoMap["base"]["onto"]], taskOperatorArgument, self.getOASISEntityByName("overloads"), object)
                break
            # mapping the task object, input, and output
            for elem in mapping[1:]:
               for map in elem:
                  self.addObjPropAssertion(self.ontologies[self.ontoMap["base"]["onto"]], URIRef(self.ontoMap["base"]["namespace"]+map[0]), self.getOASISEntityByName("overloads"), URIRef(self.ontoMap["template"]["namespace"]+map[1]))


    #create and link an action to the agent responsible for it
    #  behaviorName, goalName, taskName, operators, operatorsArguments, objects, inputs,  outputs, mapping):
    def createAgentAction(self, agentname, planName, goalName, taskName, operators, operatorsArguments, objects, inputs, outputs, mapping):
        agent=self.ontoMap["base"]["namespace"]+agentname
        plan, goal, task, taskOperator, taskOperatorArgument = self.__createExecutionPath__(self.ontologies[self.ontoMap["action"]["onto"]],
                                                                                           self.ontoMap["action"]["namespace"],
                                                                                           planName, "PlanExecution",
                                                                                           goalName, taskName, operators, operatorsArguments)

        self.addObjPropAssertion(self.ontologies[self.ontoMap["action"]["onto"]], agent, self.getOASISEntityByName("performs"), task)

        if objects:
            for object in objects:
                objectName = self.addTaskObjectToTask(self.ontologies[self.ontoMap["action"]["onto"]], self.ontoMap["action"]["namespace"], task, object[0], object[1], object[2])

        # create, add, and connect the task input parameters
        if inputs:
           for input in inputs:
               inputName = self.addTaskActualInputToTask(self.ontologies[self.ontoMap["action"]["onto"]], self.ontoMap["action"]["namespace"],task, input[0], input[1], input[2])

        if outputs:
           for output in outputs:
               outputName = self.addTaskActualOutputToTask(self.ontologies[self.ontoMap["action"]["onto"]], self.ontoMap["action"]["namespace"], task, output[0], output[1], output[2])

        # linking agent action with the corresponding behavior template
        if mapping:
        # mapping the task
          task_op = URIRef(self.ontoMap["base"]["namespace"] + mapping[0])
          self.addObjPropAssertion(self.ontologies[self.ontoMap["action"]["onto"]], task, self.getOASISEntityByName("drawnBy"), task_op)  # the action
          # mapping the task operator (automatically)
          for object in self.ontologies[self.ontoMap["base"]["onto"]].objects(task_op, self.getOASISEntityByName("hasTaskOperator")):
              self.addObjPropAssertion(self.ontologies[self.ontoMap["action"]["onto"]], taskOperator, self.getOASISEntityByName("drawnBy"), object)
              break

          # mapping the task operator argument (automatically) #
          for object in self.ontologies[self.ontoMap["base"]["onto"]].objects(task_op, self.getOASISEntityByName("hasTaskOperatorArgument")):
              self.addObjPropAssertion(self.ontologies[self.ontoMap["action"]["onto"]], taskOperatorArgument, self.getOASISEntityByName("drawnBy"), object)
              break

          # mapping the task object, input, and output
          for elem in mapping[1:]:
             for map in elem:
                 self.addObjPropAssertion(self.ontologies[self.ontoMap["action"]["onto"]],
                                                    URIRef(self.ontoMap["action"]["namespace"] + map[0]), self.getOASISEntityByName("drawnBy"),
                                                    URIRef(self.ontoMap["base"]["namespace"] + map[1]))

        return

    def createAgentPlanDescription(self, agentname, planName, goalName, taskName, operators, operatorsArguments,
                        objects, inputs, outputs):
        return self.createAgentPlan(agentname, self.getOASISEntityByName("requests"), planName, "PlanDescription", goalName, taskName, operators, operatorsArguments, objects, inputs,  outputs)

    def createAgentPlan(self, agentname, propertyAgent, planName, planClass, goalName, taskName, operators, operatorsArguments, objects, inputs,  outputs):
        agent = self.ontoMap["base"]["namespace"] + agentname;
        plan, goal, task, taskOperator, taskOperatorArgument = self.__createPlanPath__( self.ontologies[self.ontoMap["plan"]["onto"]],
                                                                                             self.ontoMap["plan"]["namespace"],
                                                                                             planName, planClass, goalName, taskName, operators, operatorsArguments)

        self.addObjPropAssertion(self.ontologies[self.ontoMap["plan"]["onto"]], agent, propertyAgent, plan)

        # create, add, and connect the task input parameters
        if inputs:
            for input in inputs:
                inputName = self.addTaskFormalInputToPlanTask(task, input[0], input[1], input[2])

        # create, add, and connect the task input parameters
        if outputs:
            for output in outputs:
                outputName = self.addTaskFormalOutputToPlanTask(task, output[0], output[1], output[2])
        return

    def getTemplateOntology(self):
         return self.ontologies[self.ontoMap["template"]["onto"]]

    def getAgentOntology(self):
         return self.ontologies[self.ontoMap["base"]["onto"]]