# coding: utf-8
import twilio
from twilio.rest import Client
import random

# Account SID and Auth Token from twilio.com/console
account_sid = "AC9e2b74d77fc9244a8ac2275f057ce21b"
auth_token = "9180454f2742ba35cf63a47e9e7897b0"
client = Client(account_sid, auth_token)

# Main Event - comment out later
def lambda_handler(event, context):
    # ClickType and file name
    clickType = event['clickType']
    file = ""

    # File selection
    if clickType == 'SINGLE':
        file = puppyPic()
    elif clickType == 'DOUBLE':
        file = kittyPic()
    elif clickType == 'LONG':
        file = otherPic()

    # URL to image file 
    media = ('https://s3.us-east-2.amazonaws.com/puppyproject/%s.jpg' % file)
        
    # send MMS

    client.messages.create(
    to="+14695796898",
    from_="+14694164960",
    body="hashtag adorbs",
    media_url=media)
                    
    print('Done!')

# Picture functions - temp placement
def puppyPic():
    puppies = [
    'puppy_001', 
    'puppy_002', 
    'puppy_003', 
    'puppy_004', 
    'puppy_005', 
    'puppy_006', 
    'puppy_007', 
    'puppy_008', 
    'puppy_009', 
    'puppy_010', 
    'puppy_011', 
    'puppy_012', 
    'puppy_013', 
    'puppy_014', 
    'puppy_015', 
    'puppy_016', 
    'puppy_017', 
    'puppy_018', 
    'puppy_019', 
    'puppy_020', 
    'puppy_021', 
    'puppy_022', 
    'puppy_023', 
    'puppy_024', 
    'puppy_025', 
    'puppy_026', 
    'puppy_027', 
    'puppy_028', 
    'puppy_029', 
    'puppy_030', 
    'puppy_031', 
    'puppy_032', 
    'puppy_033', 
    'puppy_034', 
    'puppy_035', 
    'puppy_036', 
    'puppy_037', 
    'puppy_038', 
    'puppy_039', 
    'puppy_040', 
    'puppy_041', 
    'puppy_042', 
    'puppy_043', 
    'puppy_044', 
    'puppy_045', 
    'puppy_046', 
    'puppy_047', 
    'puppy_048', 
    'puppy_049',
    'puppy_050']
    return random.choice(puppies)

def kittyPic():
    kitties = [
    'kitty_001',
    'kitty_002',
    'kitty_003',
    'kitty_004',
    'kitty_005',
    'kitty_006',
    'kitty_007',
    'kitty_008',
    'kitty_009',
    'kitty_010',
    'kitty_011',
    'kitty_012',
    'kitty_013',
    'kitty_014',
    'kitty_015',
    'kitty_016',
    'kitty_017',
    'kitty_018',
    'kitty_019',
    'kitty_020',
    'kitty_021',
    'kitty_022',
    'kitty_023',
    'kitty_024',
    'kitty_025',
    'kitty_026',
    'kitty_027',
    'kitty_028',
    'kitty_029',
    'kitty_030']
    return random.choice(kitties)

def otherPic():
    others=[
    'other_001',
    'other_002',
    'other_003',
    'other_004',
    'other_005',
    'other_006',
    'other_007',
    'other_008',
    'other_009',
    'other_010',
    'other_011',
    'other_012',
    'other_013',
    'other_014',
    'other_015',
    'other_016',
    'other_017',
    'other_018',
    'other_019',
    'other_020',
    'other_021',
    'other_022',
    'other_023',
    'other_024',
    'other_025',
    'other_026',
    'other_027',
    'other_028',
    'other_029',
    'other_030']
    return random.choice(others)
