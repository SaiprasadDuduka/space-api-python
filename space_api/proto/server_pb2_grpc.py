# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from space_api.proto import server_pb2 as server__pb2


class SpaceCloudStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/proto.SpaceCloud/Create',
        request_serializer=server__pb2.CreateRequest.SerializeToString,
        response_deserializer=server__pb2.Response.FromString,
        )
    self.Read = channel.unary_unary(
        '/proto.SpaceCloud/Read',
        request_serializer=server__pb2.ReadRequest.SerializeToString,
        response_deserializer=server__pb2.Response.FromString,
        )
    self.Update = channel.unary_unary(
        '/proto.SpaceCloud/Update',
        request_serializer=server__pb2.UpdateRequest.SerializeToString,
        response_deserializer=server__pb2.Response.FromString,
        )
    self.Delete = channel.unary_unary(
        '/proto.SpaceCloud/Delete',
        request_serializer=server__pb2.DeleteRequest.SerializeToString,
        response_deserializer=server__pb2.Response.FromString,
        )
    self.Aggregate = channel.unary_unary(
        '/proto.SpaceCloud/Aggregate',
        request_serializer=server__pb2.AggregateRequest.SerializeToString,
        response_deserializer=server__pb2.Response.FromString,
        )
    self.Batch = channel.unary_unary(
        '/proto.SpaceCloud/Batch',
        request_serializer=server__pb2.BatchRequest.SerializeToString,
        response_deserializer=server__pb2.Response.FromString,
        )
    self.Call = channel.unary_unary(
        '/proto.SpaceCloud/Call',
        request_serializer=server__pb2.FunctionsRequest.SerializeToString,
        response_deserializer=server__pb2.Response.FromString,
        )
    self.RealTime = channel.stream_stream(
        '/proto.SpaceCloud/RealTime',
        request_serializer=server__pb2.RealTimeRequest.SerializeToString,
        response_deserializer=server__pb2.RealTimeResponse.FromString,
        )
    self.Service = channel.stream_stream(
        '/proto.SpaceCloud/Service',
        request_serializer=server__pb2.FunctionsPayload.SerializeToString,
        response_deserializer=server__pb2.FunctionsPayload.FromString,
        )
    self.Profile = channel.unary_unary(
        '/proto.SpaceCloud/Profile',
        request_serializer=server__pb2.ProfileRequest.SerializeToString,
        response_deserializer=server__pb2.Response.FromString,
        )
    self.Profiles = channel.unary_unary(
        '/proto.SpaceCloud/Profiles',
        request_serializer=server__pb2.ProfilesRequest.SerializeToString,
        response_deserializer=server__pb2.Response.FromString,
        )
    self.EditProfile = channel.unary_unary(
        '/proto.SpaceCloud/EditProfile',
        request_serializer=server__pb2.EditProfileRequest.SerializeToString,
        response_deserializer=server__pb2.Response.FromString,
        )
    self.SignIn = channel.unary_unary(
        '/proto.SpaceCloud/SignIn',
        request_serializer=server__pb2.SignInRequest.SerializeToString,
        response_deserializer=server__pb2.Response.FromString,
        )
    self.SignUp = channel.unary_unary(
        '/proto.SpaceCloud/SignUp',
        request_serializer=server__pb2.SignUpRequest.SerializeToString,
        response_deserializer=server__pb2.Response.FromString,
        )
    self.CreateFolder = channel.unary_unary(
        '/proto.SpaceCloud/CreateFolder',
        request_serializer=server__pb2.CreateFolderRequest.SerializeToString,
        response_deserializer=server__pb2.Response.FromString,
        )
    self.ListFiles = channel.unary_unary(
        '/proto.SpaceCloud/ListFiles',
        request_serializer=server__pb2.ListFilesRequest.SerializeToString,
        response_deserializer=server__pb2.Response.FromString,
        )
    self.DeleteFile = channel.unary_unary(
        '/proto.SpaceCloud/DeleteFile',
        request_serializer=server__pb2.DeleteFileRequest.SerializeToString,
        response_deserializer=server__pb2.Response.FromString,
        )
    self.UploadFile = channel.stream_unary(
        '/proto.SpaceCloud/UploadFile',
        request_serializer=server__pb2.UploadFileRequest.SerializeToString,
        response_deserializer=server__pb2.Response.FromString,
        )
    self.DownloadFile = channel.unary_stream(
        '/proto.SpaceCloud/DownloadFile',
        request_serializer=server__pb2.DownloadFileRequest.SerializeToString,
        response_deserializer=server__pb2.FilePayload.FromString,
        )
    self.PubsubPublish = channel.unary_unary(
        '/proto.SpaceCloud/PubsubPublish',
        request_serializer=server__pb2.PubsubPublishRequest.SerializeToString,
        response_deserializer=server__pb2.Response.FromString,
        )
    self.PubsubSubscribe = channel.stream_stream(
        '/proto.SpaceCloud/PubsubSubscribe',
        request_serializer=server__pb2.PubsubSubscribeRequest.SerializeToString,
        response_deserializer=server__pb2.PubsubMsgResponse.FromString,
        )


class SpaceCloudServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Create(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Read(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Aggregate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Batch(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Call(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RealTime(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Service(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Profile(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Profiles(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EditProfile(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SignIn(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SignUp(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateFolder(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListFiles(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteFile(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UploadFile(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DownloadFile(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PubsubPublish(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PubsubSubscribe(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SpaceCloudServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=server__pb2.CreateRequest.FromString,
          response_serializer=server__pb2.Response.SerializeToString,
      ),
      'Read': grpc.unary_unary_rpc_method_handler(
          servicer.Read,
          request_deserializer=server__pb2.ReadRequest.FromString,
          response_serializer=server__pb2.Response.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=server__pb2.UpdateRequest.FromString,
          response_serializer=server__pb2.Response.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=server__pb2.DeleteRequest.FromString,
          response_serializer=server__pb2.Response.SerializeToString,
      ),
      'Aggregate': grpc.unary_unary_rpc_method_handler(
          servicer.Aggregate,
          request_deserializer=server__pb2.AggregateRequest.FromString,
          response_serializer=server__pb2.Response.SerializeToString,
      ),
      'Batch': grpc.unary_unary_rpc_method_handler(
          servicer.Batch,
          request_deserializer=server__pb2.BatchRequest.FromString,
          response_serializer=server__pb2.Response.SerializeToString,
      ),
      'Call': grpc.unary_unary_rpc_method_handler(
          servicer.Call,
          request_deserializer=server__pb2.FunctionsRequest.FromString,
          response_serializer=server__pb2.Response.SerializeToString,
      ),
      'RealTime': grpc.stream_stream_rpc_method_handler(
          servicer.RealTime,
          request_deserializer=server__pb2.RealTimeRequest.FromString,
          response_serializer=server__pb2.RealTimeResponse.SerializeToString,
      ),
      'Service': grpc.stream_stream_rpc_method_handler(
          servicer.Service,
          request_deserializer=server__pb2.FunctionsPayload.FromString,
          response_serializer=server__pb2.FunctionsPayload.SerializeToString,
      ),
      'Profile': grpc.unary_unary_rpc_method_handler(
          servicer.Profile,
          request_deserializer=server__pb2.ProfileRequest.FromString,
          response_serializer=server__pb2.Response.SerializeToString,
      ),
      'Profiles': grpc.unary_unary_rpc_method_handler(
          servicer.Profiles,
          request_deserializer=server__pb2.ProfilesRequest.FromString,
          response_serializer=server__pb2.Response.SerializeToString,
      ),
      'EditProfile': grpc.unary_unary_rpc_method_handler(
          servicer.EditProfile,
          request_deserializer=server__pb2.EditProfileRequest.FromString,
          response_serializer=server__pb2.Response.SerializeToString,
      ),
      'SignIn': grpc.unary_unary_rpc_method_handler(
          servicer.SignIn,
          request_deserializer=server__pb2.SignInRequest.FromString,
          response_serializer=server__pb2.Response.SerializeToString,
      ),
      'SignUp': grpc.unary_unary_rpc_method_handler(
          servicer.SignUp,
          request_deserializer=server__pb2.SignUpRequest.FromString,
          response_serializer=server__pb2.Response.SerializeToString,
      ),
      'CreateFolder': grpc.unary_unary_rpc_method_handler(
          servicer.CreateFolder,
          request_deserializer=server__pb2.CreateFolderRequest.FromString,
          response_serializer=server__pb2.Response.SerializeToString,
      ),
      'ListFiles': grpc.unary_unary_rpc_method_handler(
          servicer.ListFiles,
          request_deserializer=server__pb2.ListFilesRequest.FromString,
          response_serializer=server__pb2.Response.SerializeToString,
      ),
      'DeleteFile': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteFile,
          request_deserializer=server__pb2.DeleteFileRequest.FromString,
          response_serializer=server__pb2.Response.SerializeToString,
      ),
      'UploadFile': grpc.stream_unary_rpc_method_handler(
          servicer.UploadFile,
          request_deserializer=server__pb2.UploadFileRequest.FromString,
          response_serializer=server__pb2.Response.SerializeToString,
      ),
      'DownloadFile': grpc.unary_stream_rpc_method_handler(
          servicer.DownloadFile,
          request_deserializer=server__pb2.DownloadFileRequest.FromString,
          response_serializer=server__pb2.FilePayload.SerializeToString,
      ),
      'PubsubPublish': grpc.unary_unary_rpc_method_handler(
          servicer.PubsubPublish,
          request_deserializer=server__pb2.PubsubPublishRequest.FromString,
          response_serializer=server__pb2.Response.SerializeToString,
      ),
      'PubsubSubscribe': grpc.stream_stream_rpc_method_handler(
          servicer.PubsubSubscribe,
          request_deserializer=server__pb2.PubsubSubscribeRequest.FromString,
          response_serializer=server__pb2.PubsubMsgResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'proto.SpaceCloud', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
