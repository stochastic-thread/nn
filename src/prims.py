class Neuron:
    def sysinfoLoad():
        sysinfo = configparser()
    def validate(msg, sysinfo):
        n_checks = sysinfo.checks
        check1 = check_msg_size(msg)


    def processResponse(self, msg):
        if incoming_mbq.status == "ON":
            messages = incoming_msq.receiveBlockFragments()
            max_fragments =
            for msg in messages:
                block_fragments = validate(msg)

    def __init__(self, state=None,prev=None,handler=None):
        self.state = state
        self.incoming = []
        self.outgoing = []
        if prev is None:
            self.prev = None
        else:
            self.incoming.append(prev)

        if handler is None:
            self.handler = lambda st: processResponse(st)
        else:
            self.handler = handler

    def memory(self, data, handler_lambda):
        if self.state is None:
            self.state = data
        else:
            handler_lambda(self.state)

class NeuronGroup:
    def __init__(self, curriculum):
        self.neurons = dict()
        self.log = dict()
        self.connection_rule_eng = "neurons link back to the previous neuron"
        self.curriculum = None

    def learn(self):
        if len(self.curriculum):
            prev = None
            for item in curriculum:
                if prev is None:
                    prev = Neuron(state=item)
                else:
                    curr = Neuron(state=item, prev=prev)
                self.neurons[item] = prev
                self.log[datetime.isoformat(datetime.now())] = item





class Environment:
    def runSimulation(self):
        integers = lambda startInt, lastInt: list(range(startInt, lastInt))



