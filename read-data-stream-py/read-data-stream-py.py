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
    MY_STREAM_NAME = "StreamFromPython"
    KINESIS_STREAM_NAME = "PythonKinesisStream"
    message = "Hello World"
    myArray = bytearray()
    myArray.extend(map(ord, message))

    while(True):
        try:
            message_list = client.read_messages(
                stream_name=MY_STREAM_NAME,
                # By default, if no options are specified, it tries to read one message from the beginning of the stream.
                options=ReadMessagesOptions(
                    desired_start_sequence_number=100,
                    # Try to read from sequence number 100 or greater. By default, this is 0.
                    min_message_count=10,
                    # Try to read 10 messages. If 10 messages are not available, then NotEnoughMessagesException is raised. By default, this is 1.
                    # Accept up to 100 messages. By default this is 1.
                    max_message_count=100,
                    read_timeout_millis=5000
                    # Try to wait at most 5 seconds for the min_messsage_count to be fulfilled. By default, this is 0, which immediately returns the messages or an exception.
                )
            )
            print("printing messsage list")
            print(message_list)

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
