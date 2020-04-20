dances = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot',
          'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']
# Expected Output
# 'Cha Cha'
# 'Foxtrot'
# 'Jive'
# 'Paso Doble'
# 'Rumba'
# 'Samba'
# 'Tango'
# 'Viennese Waltz'
# 'Waltz'


sorted_dances = sorted(dances)
print(sorted_dances)

for dance in sorted_dances:
    print(dance)
