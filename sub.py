import tldextract
import multiprocessing

def split_subdomain(domain):
    extracted_info = tldextract.extract(domain)
    main_domain = extracted_info.domain
    top_level_domain = extracted_info.suffix

    return f"{main_domain}.{top_level_domain}"

def process_domain(input_domain):
    full_domain = split_subdomain(input_domain)
    return f"{full_domain}\n"

def process_file(file_path):
    with open(file_path, 'r') as file:
        input_domains = file.read().splitlines()

    with multiprocessing.Pool() as pool:
        results = pool.map(process_domain, input_domains)

    with open('output.txt', 'w') as output_file:
        output_file.write(''.join(results))

if __name__ == "__main__":
    file_path = input("Masukkan path file input: ")
    process_file(file_path)
    print("Hasil Domain Utama telah disimpan di output.txt")
