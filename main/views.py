from django.shortcuts import render
from .models import Group, Room



def allocate_rooms(request):

    rooms = Room.objects.all()
    groups = Group.objects.all()

    context = {
        'rooms': rooms,
        'groups': groups
    }

    if request.method == 'POST':

        a_rooms = request.POST.getlist('rooms')
        a_groups = request.POST.getlist('groups')

        # Convert room and group IDs to instances
        selected_rooms = Room.objects.filter(id__in=a_rooms)
        selected_groups = Group.objects.filter(id__in=a_groups)

        # Sort the selected rooms and groups by capacity in descending order
        selected_rooms = sorted(selected_rooms, key=lambda x: x.capacity, reverse=True)
        selected_groups = sorted(selected_groups, key=lambda x: x.capacity, reverse=True)

        # Allocate groups to rooms
        allocation = []
        remaining_groups = selected_groups[:]

        # First pass: Allocate at least one group to each room
        for room in selected_rooms:
            room_capacity = room.capacity
            allocated_groups = []
            for group in remaining_groups:
                if group.capacity <= room_capacity:
                    allocated_groups.append({'name': group.group_name, 'capacity': group.capacity})
                    room_capacity -= group.capacity
                    remaining_groups = [g for g in remaining_groups if g.id != group.id]
                    break  # Move to the next room after assigning one group
            allocation.append({
                'room': room.room_name,
                'room_capacity': room.capacity,
                'groups': allocated_groups
            })

        # Second pass: Allocate remaining groups to rooms
        for allocation_item in allocation:
            room_name = allocation_item['room']
            room = Room.objects.get(room_name=room_name)
            room_capacity = room.capacity - sum(group['capacity'] for group in allocation_item['groups'])

            for group in remaining_groups:
                if group.capacity <= room_capacity:
                    allocation_item['groups'].append({'name': group.group_name, 'capacity': group.capacity})
                    room_capacity -= group.capacity
                    remaining_groups = [g for g in remaining_groups if g.id != group.id]

        context['allocation'] = allocation
        context['selected_rooms'] = a_rooms
        context['selected_groups'] = a_groups
        context['remaining_groups'] = remaining_groups

        # print('======================> \n', context)

        return render(request, 'allocate_rooms.html', context)

    return render(request, 'allocate_rooms.html', context)  