from maltego_trx.entities import Phrase
from maltego_trx.overlays import OverlayPosition, OverlayType

from maltego_trx.transform import DiscoverableTransform


class OverlayExample(DiscoverableTransform):
    """
    Returns a phrase with overlays on the graph.
    """

    @classmethod
    def create_entities(cls, request, response):
        person_name = request.Value
        entity = response.addEntity(Phrase, "Hi %s, nice to meet you!" % person_name)

        # Normally, when we create an overlay, we would reference a property name so that Maltego can then use the
        # value of that property to create the overlay. Sometimes that means creating a dynamic property, but usually
        # it's better to either use an existing property, or, if you created the Entity yourself, and only need the
        # property for the overlay, to use a hidden property. Here's an example of using a dynamic property:
        entity.addProperty('dynamic_overlay_icon_name', displayName="Name for overlay image", value="Champion")
        entity.addOverlay('dynamic_overlay_icon_name', OverlayPosition.WEST, OverlayType.IMAGE)

        # DISCOURAGED:
        # You *can* also directly supply the string value of the property, however this is not recommended. Why? If
        # the entity already has a property of the same ID (in this case, "DE"), then you would in fact be assigning the
        # value of that property, not the string "DE", which is not the intention. Nevertheless, here's an example:
        entity.addOverlay('DE', OverlayPosition.SOUTH_WEST, OverlayType.IMAGE)

        # Overlays can also be used to display extra text on an entity:
        entity.addProperty("exampleDynamicPropertyName", "Example Dynamic Property", "loose", "Maltego Overlay Testing")
        entity.addOverlay('exampleDynamicPropertyName', OverlayPosition.NORTH, OverlayType.TEXT)

        # Or a small color indicator:
        entity.addOverlay('#45e06f', OverlayPosition.NORTH_WEST, OverlayType.COLOUR)

