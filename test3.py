import os
def decode(message_file_path) -> str:
    if not os.path.exists(message_file_path):
        return ''

    ans = []
    with open(message_file_path) as file_in:
        mappings = {}
        for line in file_in:
            components = line.split(' ')
            if len(components) != 2:
                return ''
            mappings[components[0]] = components[1]

        currentIndex = 0
        stepSize = 1
        while True:
            currentIndex += stepSize
            stepSize += 1
            key = f'{currentIndex}'
            if key not in mappings:
                break
            ans.append(f'{currentIndex}-{mappings[key]}')

    return ' '.join(ans).replace('\n', '')


if __name__ == '__main__':
    print(decode('./coding_qual_input.txt'))
