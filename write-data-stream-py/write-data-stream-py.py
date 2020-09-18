import asyncio
import logging
import random
import time

from greengrasssdk.stream_manager import (
    ExportDefinition,
    KinesisConfig,
    MessageStreamDefinition,
    ReadMessagesOptions,
    ResourceNotFoundException,
    StrategyOnFull,
    StreamManagerClient,
    StreamManagerException
)


def main(logger):
    client = StreamManagerClient()
    my_stream_name = "StreamFromPython"
    kinesis_stream_name = "PythonKinesisStream"
    message = "Hello World"
    myArray = bytearray()
    myArray.extend(map(ord, message))
    
    while(True):
        try:
            sequence_number = client.append_message(stream_name=my_stream_name, data=myArray)
            print(sequence_number)
            print(type(sequence_number))
            #print("Message has been appended with sequence number: {sequence}").format(sequence = str(sequence_number))
            print("Message has been appended with sequence number" + str(sequence_number))
        except StreamManagerException as smeError:
            print("getting stream manager exception")
            print(smeError)
        except ConnectionError or asyncio.TimeoutError as cError:
            print("getting connection error")
            print(cError)

        time.sleep(5)
        

def function_handler(event, context):
    return


logging.basicConfig(level=logging.INFO)
# Starting main
main(logger=logging.getLogger())
