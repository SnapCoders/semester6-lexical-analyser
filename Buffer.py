class Buffer:
    def load_buffer(self):
        file = open('program.c', 'r')
        file_buffer = file.readline()
        buffer = []
        cont = 1

        while file_buffer != "":
            buffer.append(file_buffer)
            file_buffer = file.readline()
            cont += 1

            if cont == 10 or file_buffer == '':
                # Return a full buffer
                temp_buf = ''.join(buffer)
                cont = 1
                '''
                When you use a function with a return value, every time you call the function, it starts with a new set of variables. 
                In contrast, if you use a generator function instead of a normal function, the execution will start right from where it left last.
                '''
                yield temp_buf

                # Reset the buffer
                buffer = []

        file.close()
