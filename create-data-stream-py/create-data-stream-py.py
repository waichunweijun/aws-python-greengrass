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
    stream_name = "StreamFromPython"
    kinesis_stream_name = "PythonKinesisStream"
    try:
        client.create_message_stream(MessageStreamDefinition(
            name=stream_name,  # Required.
            max_size=268435456,  # Default is 256 MB.
            stream_segment_size=16777216,  # Default is 16 MB.
            time_to_live_millis=None,  # By default, no TTL is enabled.
            strategy_on_full=StrategyOnFull.OverwriteOldestData,  # Required.
            flush_on_write=False,  # Default is false.
            export_definition=ExportDefinition(  # Optional. Choose where/how the stream is exported to the AWS Cloud.
                kinesis=None,
                iot_analytics=None
            )
        ))
    except StreamManagerException as smeError:
        print(smeError)
        pass
        
    except ConnectionError or asyncio.TimeoutError as cError:
        print(cError)
        pass
        

def function_handler(event, context):
    return


logging.basicConfig(level=logging.INFO)
# Starting main
main(logger=logging.getLogger())
