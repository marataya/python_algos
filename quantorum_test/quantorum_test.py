import re
import json

def holiday (input_list = ['dream', 'party']) :
    input_list[0], input_list[-1] = input_list[-1], input_list[0]
    return input_list


if __name__ == '__main__':

    text = '''
    Apache Airflow is an open-source workflow management platform for data engineering pipelines. It started at Airbnb in October 2014 as a solution to manage the company's increasingly complex workflows. Creating Airflow allowed Airbnb to programmatically author and schedule their workflows and monitor them via the built-in Airflow user interface. From the beginning, the project was made open source, becoming an Apache Incubator project in March 2016 and a Top-Level Apache Software Foundation project in January 2019. Airflow is written in Python, and workflows are created via Python scripts. Airflow is designed under the principle of "configuration as code". While other "configuration as code" workflow platforms exist using markup languages like XML, using Python allows developers to import libraries and classes to help them create their workflows. Airflow uses directed acyclic graphs (DAGs) to manage workflow orchestration. Tasks and dependencies are defined in Python and then Airflow manages the scheduling and execution. DAGs can be run either on a defined schedule (e.g. hourly or daily) or based on external event triggers (e.g. a file appearing in Hive). Previous DAG-based schedulers like Oozie and Azkaban tended to rely on multiple configuration files and file system trees to create a DAG, whereas in Airflow, DAGs can often be written in one Python file. Three notable providers offer ancillary services around the core open source project. Astronomer has built a SaaS tool and Kubernetes-deployable Airflow stack that assists with monitoring, alerting, devops, and cluster management. Cloud Composer is a managed version of Airflow that runs on Google Cloud Platform (GCP) and integrates well with other GCP services. Starting from November 2020, Amazon Web Services offers Managed Workflows for Apache Airflow.
    '''
    freqs = {}
    for word in text.split():
        # print(re.sub('[^A-Za-z]', '', word))
        sanitized_word = re.sub('[^A-Za-z]', '', word)
        freqs[sanitized_word] = freqs.get(sanitized_word, 0) + 1
    print(sorted(freqs.items(), key=lambda x: x[1]))

    with open('input.json', 'r') as f:
        data = json.load(f)

    records = [record for record in data['root'] if record['id'] == 'user09']

    e_count = 0
    h_count = 0

    for record in records:
        if 'codes' in record:
            for code in record['codes']:
                e_count += code.count('E')
                h_count += code.count('H')

    print(f"The character 'E' appears {e_count} times.")
    print(f"The character 'H' appears {h_count} times.")

    panda = ['bamboo', 'python' ]
    student = panda
    print(panda)
    panda [0] = 'leaf'
    print(panda)
    student[1] = 'algorithm'
    print(student)
    student = holiday()
    print(student)
    print(panda)
    student.append(panda[1])
    print(student)
    print(panda)
    panda = holiday()
    print(panda)


# print("Hi, {}! My name is {}.".format("Mark", "World"))

# print("Hi, {target}! My name is {name}.".format(name="Mark", target="World"))
#
#

# print(name = "Mark" target = "World" f"Hi, {target}! My name is {name}.")

# print(name = "Mark" target = "World" `Hi, {target}! My name is {name}.`)
#
# print("Hi, %i! My name is %s." % "World" % "Mark")
#
# print("Hi, %(target)s! My name is %(name)s" % {"target": "World", "name": "Mark"})
