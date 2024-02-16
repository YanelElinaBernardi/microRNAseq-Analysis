import os
import subprocess

def assembly(input_folder):
    archivos_trimm = [f for f in os.listdir(input_folder) if f.endswith('_trimm.fastq')]
    for archivo in archivos_trimm:
        flye = f"flye --nano-raw {archivo} --out-dir flye_{archivo.split('_')[0]} --threads 4"
        subprocess.run(flye, shell=True)

def qc_assembly(input_folder):
    carpetas_flye = [f for f in os.listdir(input_folder) if f.startswith('flye_')]
    for carpeta_flye in carpetas_flye:
        quast = f"quast.py {os.path.join(carpeta_flye, 'assembly.fasta')} -o quast_{carpeta_flye.split('_')[1]}"
        subprocess.run(quast, shell=True)

if __name__ == "__main__":
    input_folder = "/home/yanel/prueba_ont/"  
    assembly(input_folder)
    qc_assembly(input_folder)
