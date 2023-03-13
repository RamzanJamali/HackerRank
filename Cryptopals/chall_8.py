def count_repts(citext, block_size):
    chunks = [citext[i:i+block_size] for i in range(0, len(citext), block_size)]
    num_of_repts = len(chunks) - len(set(chunks))
    result = {
        'ciphertext' : citext,
        'repetitions' : num_of_repts
        }
    return result

citext = [bytes.fromhex(line.strip()) for line in open('chall_8.txt')]
block_size = 16
repetitions = [count_repts(cipher, block_size) for cipher in citext]

most_repetitions = sorted(repetitions, key = lambda x: x['repetitions'], reverse = True)[0]

print("Ciphertext:{}".format(most_repetitions['ciphertext']))
print("Repeating Blocks:{}".format(most_repetitions['repetitions']))
