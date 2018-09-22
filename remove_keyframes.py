import bpy

STEP_SIZE = 10

print("Start-----------------------------")
channels = bpy.context.active_object.animation_data.action.groups[1].channels
for channel in channels:
    print('Channel: {}, select: {}, index:{}'.format(channel.data_path, channel.select, channel.array_index))
    keyframePoints = channel.keyframe_points
    if not channel.select:
        continue
    deleteFrameList = []
    for i in range(0, len(keyframePoints)):
        frame = keyframePoints[i].co[0]
        print('Frame: {}, modular: {}'.format(frame, frame % STEP_SIZE > 0))
        if frame % STEP_SIZE > 0:
            deleteFrameList.append(frame)
    for deleteFrame in deleteFrameList:
        print('Delete frame: {}'.format(deleteFrame))
        bpy.context.active_object.keyframe_delete(channel.data_path, frame=deleteFrame, index=channel.array_index)
