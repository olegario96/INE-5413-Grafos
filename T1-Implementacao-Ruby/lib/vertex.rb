require 'set'

class Vertex
  attr_reader :data
  attr_accessor :neighbours

  def initialize(data)
    @data = data
    @neighbours = Set.new
  end

  def degree
    self.neighbours.size
  end

  def are_neighbours?(vertex)
    self.neighbours.member?(vertex)
  end

  def has_neighbours?
    !self.neighbours.empty?
  end

  def check_data(data)
    return self.data == data
  end

  def to_s
    puts "Data: #{self.data}"
    # print 'Neighbours: '
    # self.neighbours.each do |neighbour|
    #   puts "#{neighbour}"
    # end
  end
end
