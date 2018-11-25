def validate_card(args):
    errors = []
    if len(args['cardNumber']) != 16:
        errors.append(
            {'cardNumber': 'number has 16 chars'}
        )
    if len(args['expirationYear']) != 4:
        errors.append(
            {'expirationYear': 'number has 4 chars'}
        )
    if len(args['expirationMonth']) != 2:
        errors.append(
            {'expirationMonth': 'number has 2 chars'}
        )
    if len(args['cvc']) != 3:
        errors.append(
            {'cvc': 'number has 3 chars'}
        )
    if errors == []:
        errors = None
    return errors

def validate_seller(args):
    errors = []
    if not '@' in args['email']:
        errors.append(
            {'email': 'it isnt'}
        )
    if errors == []:
        errors = None


